from omegaconf import OmegaConf


def read_config_file(file_path) -> dict | list:
    cfg = OmegaConf.load(file_path)
    return cfg


def convert_to_container(conf) -> dict:
    conf = OmegaConf.to_container(conf)
    return conf
