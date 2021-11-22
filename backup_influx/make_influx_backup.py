#!/usr/bin/python3

import subprocess
import paramiko
import time

from datetime import datetime

def main():
    """
    Main function in backup script.
    """
    # Ssh credentials and config
    username = "pi"
    hostname = "192.168.100.239"
    backup_username = "patrykmodzelewski"
    port = 22
    UseGSSAPI = (
        paramiko.GSS_AUTH_AVAILABLE
    )  # enable "gssapi-with-mic" authentication, if supported by your python installation
    DoGSSAPIKeyExchange = (
        paramiko.GSS_AUTH_AVAILABLE
    )
    archive = ".tar.gz"

    # Prepeare command config
    now = datetime.now()
    timestamp = now.strftime("/%d-%m-%y_%H:%M:%S")
    dst_dir = "/Users/patrykmodzelewski/Projects/lora_mgr_project/backup_influx/backups"
    src_dir = "/home/pi/lora_mgr_project/influx/backups"
    dst_file = f"{dst_dir}/{timestamp}"
    src_file = f"{src_dir}/{timestamp}"
    commands = {
        "backup":
            f"docker exec -it lora_mgr_project_influxdb_1\
                influxd backup -portable /tmp/backups/{timestamp}"
        ,
        "ownership": f"sudo chmod 777 {src_file}",
        "archieve": f"sudo tar -zcvf {src_file}{archive} {src_file}"
    }

    try:
        # Connect to computer
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())
        client.connect(
            hostname,
            port,
            username,
            gss_auth=UseGSSAPI,
            gss_kex=DoGSSAPIKeyExchange,
        )

        chan = client.invoke_shell()
        for command in commands:
            print(command + " ... ")
            output = send_command(chan, cmd=commands[command])
        get_backup(client, src_file + ".tar.gz", dst_file + ".tar.gz")
        chan.close()
        client.close()

    except Exception as e:
        print(f"{e} {e.__class__}")


def send_command(remote_conn, cmd="", delay=1):
    """
    Send command down the channel. Retrieve and return the output.
    """

    MAX_BUFFER=65000
    if cmd != "":
        cmd = cmd.strip()
    remote_conn.send(cmd + '\n')
    time.sleep(delay)

    if remote_conn.recv_ready():
        return remote_conn.recv(MAX_BUFFER)
    else:
        return ""

def get_backup(ssh_client, src, dst):
    """
    Get file from server.
    """

    ftp_client = ssh_client.open_sftp()
    ftp_client.get(src, dst)
    ftp_client.close()

def put_backup(ssh_client, src, dst):
    """
    Put file on server.
    """

    ftp_client = ssh_client.open_sftp()
    ftp_client.put(src, dst)
    ftp_client.close()

main()
