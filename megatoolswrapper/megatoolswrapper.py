import logging
import subprocess

logger = logging.getLogger("megatools_wrapper")


class MegaToolsWrapper:
    megatools_path = ""

    def __init__(self, megatools_path=""):
        self.megatools_path = megatools_path

    def megacopy(self, mega_link, limit_speed=0, path="./"):
        """
        Usage:
            megacopy.exe [OPTION▒] - synchronize local and remote mega.nz directories

        Help Options:
            -h, --help                  Show help options
            --help-all                  Show all help options

        Application Options:
          -r, --remote=PATH           Remote directory
          -l, --local=PATH            Local directory
          -d, --download              Download files from mega
          --no-progress               Disable progress bar
          --no-follow                 Don't follow symbolic links
          -n, --dryrun                Don't perform any actual changes
          --enable-previews           Generate previews when uploading file
          --disable-previews          Never generate previews when uploading file
          --disable-resume            Disable resume when downloading file
          -u, --username=USERNAME     Account username (email)
          -p, --password=PASSWORD     Account password
          --no-ask-password           Never ask interactively for a password
          --reload                    Reload filesystem cache
          --limit-speed=SPEED         Limit transfer speed (KiB/s)
          --proxy=PROXY               Proxy setup string
          --config=PATH               Load configuration from a file
          --ignore-config-file        Disable loading mega.ini
          --debug=OPTS                Enable debugging output
          --version                   Show version information
        """

        command = f"{self.megatools_path}megacopy {mega_link} --limit-speed={limit_speed} --path={path}"

        logger.debug(command)

        return_code = execute_command(command)

        logger.debug(return_code)

    def megadf(self, mega_link, limit_speed=0, path="./"):
        """
        Usage:
            megadf.exe [OPTION▒] - display mega.nz storage quotas/usage

        Help Options:
            -?, --help                  Show help options
            --help-all                  Show all help options

        Application Options:
            -h, --human                 Use human readable formatting
            --mb                        Show numbers in MiB
            --gb                        Show numbers in GiB
            --total                     Show only total available space
            --used                      Show only used space
            --free                      Show only available free space
            -u, --username=USERNAME     Account username (email)
            -p, --password=PASSWORD     Account password
            --no-ask-password           Never ask interactively for a password
            --reload                    Reload filesystem cache
            --limit-speed=SPEED         Limit transfer speed (KiB/s)
            --proxy=PROXY               Proxy setup string
            --config=PATH               Load configuration from a file
            --ignore-config-file        Disable loading mega.ini
            --debug=OPTS                Enable debugging output
            --version                   Show version information
        """

        command = f"{self.megatools_path}megacopy {mega_link} --limit-speed={limit_speed} --path={path}"

        logger.debug(command)

        return_code = execute_command(command)

        logger.debug(return_code)

    def megadl(self, mega_link, limit_speed=0, path="./"):
        """
        Usage:
            megadl.exe [OPTION▒] - download exported files from mega.nz

        Help Options:
            -h, --help                  Show help options
            --help-all                  Show all help options

        Application Options:
            --path=PATH                 Local directory or file name, to save data to
            --no-progress               Disable progress bar
            --print-names               Print names of downloaded files
            --choose-files              Choose which files to download when downloading folders (interactive)
            --disable-resume            Disable resume when downloading file
            -u, --username=USERNAME     Account username (email)
            -p, --password=PASSWORD     Account password
            --no-ask-password           Never ask interactively for a password
            --reload                    Reload filesystem cache
            --limit-speed=SPEED         Limit transfer speed (KiB/s)
            --proxy=PROXY               Proxy setup string
            --config=PATH               Load configuration from a file
            --ignore-config-file        Disable loading mega.ini
            --debug=OPTS                Enable debugging output
            --version                   Show version information
        """

        command = f"{self.megatools_path}megadl {mega_link} --limit-speed={limit_speed} --path={path}"

        logger.debug(command)

        return_code = execute_command(command)

        logger.debug(return_code)

    def megaget(self, mega_link, limit_speed=0, path="./"):
        """
        Usage:
            megaget.exe [OPTION▒] - download individual files from mega.nz

        Help Options:
            -h, --help                  Show help options
            --help-all                  Show all help options

        Application Options:
            --path=PATH                 Local directory or file name, to save data to
            --no-progress               Disable progress bar
            --disable-resume            Disable resume when downloading file
            -u, --username=USERNAME     Account username (email)
            -p, --password=PASSWORD     Account password
            --no-ask-password           Never ask interactively for a password
            --reload                    Reload filesystem cache
            --limit-speed=SPEED         Limit transfer speed (KiB/s)
            --proxy=PROXY               Proxy setup string
            --config=PATH               Load configuration from a file
            --ignore-config-file        Disable loading mega.ini
            --debug=OPTS                Enable debugging output
            --version                   Show version information
        """

        command = f"{self.megatools_path}megacopy {mega_link} --limit-speed={limit_speed} --path={path}"

        logger.debug(command)

        return_code = execute_command(command)

        logger.debug(return_code)

    def megals(self, mega_link, limit_speed=0, path="./"):
        """
        Usage:
          megals.exe [OPTION▒] - list files stored at mega.nz

        Help Options:
          -?, --help                  Show help options
          --help-all                  Show all help options

        Application Options:
          -n, --names                 List names of files only (will be disabled if you                                                                                                                                                                                                specify multiple paths)
          -R, --recursive             List files in subdirectories
          -l, --long                  Use a long listing format
          --header                    Show columns header in long listing
          -h, --human                 Human readable sizes
          -0, --print0                Separate file paths with NULs
          -e, --export                Show mega.nz download links (export)
          -u, --username=USERNAME     Account username (email)
          -p, --password=PASSWORD     Account password
          --no-ask-password           Never ask interactively for a password
          --reload                    Reload filesystem cache
          --limit-speed=SPEED         Limit transfer speed (KiB/s)
          --proxy=PROXY               Proxy setup string
          --config=PATH               Load configuration from a file
          --ignore-config-file        Disable loading mega.ini
          --debug=OPTS                Enable debugging output
          --version                   Show version information
        """

        command = f"{self.megatools_path}megacopy {mega_link} --limit-speed={limit_speed} --path={path}"

        logger.debug(command)

        return_code = execute_command(command)

        logger.debug(return_code)

    def megamkdir(self, mega_link, limit_speed=0, path="./"):
        """
        Usage:
            megamkdir.exe [OPTION▒] - create directories at mega.nz

        Help Options:
            -h, --help                  Show help options
            --help-all                  Show all help options

        Application Options:
            -u, --username=USERNAME     Account username (email)
            -p, --password=PASSWORD     Account password
            --no-ask-password           Never ask interactively for a password
            --reload                    Reload filesystem cache
            --limit-speed=SPEED         Limit transfer speed (KiB/s)
            --proxy=PROXY               Proxy setup string
            --config=PATH               Load configuration from a file
            --ignore-config-file        Disable loading mega.ini
            --debug=OPTS                Enable debugging output
            --version                   Show version information
        """
        command = f"{self.megatools_path}megacopy {mega_link} --limit-speed={limit_speed} --path={path}"

        logger.debug(command)

        return_code = execute_command(command)

        logger.debug(return_code)

    def megaput(self, mega_link, limit_speed=0, path="./"):
        """
        Usage:
            megaput.exe [OPTION▒] - upload files to mega.nz

            Help Options:
            -h, --help                  Show help options
            --help-all                  Show all help options

        Application Options:
            --path=PATH                 Remote path to save files to
            --no-progress               Disable progress bar
            --enable-previews           Generate previews when uploading file
            --disable-previews          Never generate previews when uploading file
            -u, --username=USERNAME     Account username (email)
            -p, --password=PASSWORD     Account password
            --no-ask-password           Never ask interactively for a password
            --reload                    Reload filesystem cache
            --limit-speed=SPEED         Limit transfer speed (KiB/s)
            --proxy=PROXY               Proxy setup string
            --config=PATH               Load configuration from a file
            --ignore-config-file        Disable loading mega.ini
            --debug=OPTS                Enable debugging output
            --version                   Show version information
        """

        command = f"{self.megatools_path}megacopy {mega_link} --limit-speed={limit_speed} --path={path}"

        logger.debug(command)

        return_code = execute_command(command)

        logger.debug(return_code)

    def megareg(self, mega_link, limit_speed=0, path="./"):
        """
        Usage:
            megareg.exe [OPTION▒] LINK - register a new mega.nz account

        Help Options:
            -h, --help                  Show help options
            --help-all                  Show all help options

        Application Options:
            -n, --name=NAME             Your real name
            -e, --email=EMAIL           Your email (will be your username)
            -p, --password=PASSWORD     Your password
            --register                  Perform registration
            --verify=STATE              Finish registration (pass verification link)
            --scripted                  Return script friendly output from --register
            --limit-speed=SPEED         Limit transfer speed (KiB/s)
            --proxy=PROXY               Proxy setup string
            --config=PATH               Load configuration from a file
            --ignore-config-file        Disable loading mega.ini
            --debug=OPTS                Enable debugging output
            --version                   Show version information
        """

        command = f"{self.megatools_path}megacopy {mega_link} --limit-speed={limit_speed} --path={path}"

        logger.debug(command)

        return_code = execute_command(command)

        logger.debug(return_code)

    def megarm(self, mega_link, limit_speed=0, path="./"):
        """
        Usage:
            megarm.exe [OPTION▒] - remove files from mega.nz

        Help Options:
            -h, --help                  Show help options
            --help-all                  Show all help options

        Application Options:
            -u, --username=USERNAME     Account username (email)
            -p, --password=PASSWORD     Account password
            --no-ask-password           Never ask interactively for a password
            --reload                    Reload filesystem cache
            --limit-speed=SPEED         Limit transfer speed (KiB/s)
            --proxy=PROXY               Proxy setup string
            --config=PATH               Load configuration from a file
            --ignore-config-file        Disable loading mega.ini
            --debug=OPTS                Enable debugging output
            --version                   Show version information
        """

        command = f"{self.megatools_path}megacopy {mega_link} --limit-speed={limit_speed} --path={path}"

        logger.debug(command)

        return_code = execute_command(command)

        logger.debug(return_code)


def execute_command(command):
    process = subprocess.Popen(
        command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    process.wait()
    return process.returncode


if __name__ == "__main__":
    formatter = logging.Formatter(
        "%(asctime)s :: %(module)s :: %(lineno)s :: %(funcName)s :: %(message)s"
    )
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)

    logger.addHandler(stream_handler)

    megatools_wrapper = MegaToolsWrapper(megatools_path="C:\\megatools\\")

    megatools_wrapper.download("", limit_speed=0, path="./toto.txt")
