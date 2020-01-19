import click
import os

@click.command()
@click.option("--in", "-i", "path_to_image", required=True,
    help="Path to input image file to be processed by baby detection and classification ML model.\
        Should be a .jpg file",
    type=click.Path(exists=True, dir_okay=False, readable=True))

@click.option("--out", "-o", "out_file", default="./output.jpg",
    help="Path to output image file after processing by ML model.",
    type=click.Path(dir_okay=False))

def process(path_to_image, out_file):
    """ Apply detection and classification ML model to the input image IN and stores the result to 
    output file OUT.
    """
    from keras_yolo3.yolo import YOLO
    from PIL import Image

    # Create an instance of YOLO. In fact, its name is YOLO but this implementation already contains
    # the custom network for classification, hence it returns a image already with the classification!
    yolo_model = YOLO()
    # Notice that there will be some warnings displayed regarding instantiating YOLO, but it's not
    # important by now, it should work fine

    # Load image
    image = Image.open(path_to_image)

    # Apply network to image
    image_result, result_list = yolo_model.detect_image(image)

    # Save the generated image on same directory, with name: "result_image.jpg"
    print("***")
    print("Saving image to: '{}'".format(out_file))
    try:
        image_result.save(out_file)
        print("Success! Image saved at: {}".format(out_file))
    except Exception as e:
        print("An error occurred while trying to save image to '{}': {}".format(out_file, str(e)))

if __name__ =="__main__":
    process()