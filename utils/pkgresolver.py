import os
import logging


def resolvdep(deps: list):
    """Function to check & install debian dependencies

    Args:
        deps (list): dependencies in standard python list format

    ENV:
        FORCE_RESOLV_DEPS : set this os environment varibale to force install missing dependencies

    Returns:
        1: when missing dependencie
        2: when installation failed
        0: normal successfull exit
    """
    missing_deps    =   None
    installdeps     =   None

    for dep in deps:
        if os.WEXITSTATUS(os.system(f"which {dep} >> /dev/null")):
            logging.info(f"{dep} found in path.")
            
            if os.getenv('FORCE_RESOLV_DEPS') is not None:
                installdeps += dep
            else:
                missing_deps += dep
                logging.warning(f"Missing dependencie {dep}.")

    # check if any missing dependencies
    if missing_deps is not None:
        return 1

    # finally try to install dependencies
    if installdeps is not None:
        logging.info(f"Installing dependencies: [{installdeps}]")
        if os.WEXITSTATUS(os.system(f"apt install -y {installdeps}")) != 0:
            return 2
    else:
        return 0
