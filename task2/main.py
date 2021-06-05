import click

from image_uploader.uploader import Uploader


@click.command()
@click.argument("dir_path")
def start(dir_path: str):
    uploader = Uploader(dir_path)
    uploader.upload()


if __name__ == "__main__":
    start()
