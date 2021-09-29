if __name__ == '__main__':
    import math
    import os
    import random
    id = random.randint(1000_0000, 9999_9999)
    random.seed(id)

    from PIL import Image, ImageDraw

    WIDTH, HEIGHT = 3000, 1000
    BOX_SIZE = 10
    X_DIM, Y_DIM = (int)(WIDTH / BOX_SIZE), (int)(HEIGHT / BOX_SIZE)


    COLORS = [
        (255, 190, 41),
        (141, 21, 58),
        (235, 116, 0),
        (0, 83, 78),
        (0, 0, 0),
    ]

    img = Image.new("RGBA", (WIDTH, HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(img)


    for i in range(0, 70):

        try:
            x1 = random.randint(0, WIDTH - BOX_SIZE)
            y1 = random.randint(0, HEIGHT - BOX_SIZE)

            max_dim = min(WIDTH - x1, HEIGHT - y1)
            dim = (int)(random.randint(BOX_SIZE, max_dim - 1))

            x2 = x1 + dim
            y2 = y1 + dim

            color = COLORS[random.randint(0, len(COLORS) - 1)]
            if random.random() > 0.5:
                draw.rectangle(
                    ((x1, y1), (x2, y2)),
                    outline=color,
                    width=10,
                )
            else:
                draw.ellipse(
                    (x1, y1, x2, y2),
                    outline=color,
                    width=10,
                )
        except ValueError:
            pass

    image_file = f'/Users/nuwan.senaratna/Desktop/pil-art.squares-and-circles.{id}.png'
    img.save(image_file, 'PNG')
    os.system(f'open {image_file}')
