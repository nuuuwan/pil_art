if __name__ == '__main__':
    import random

    from PIL import Image, ImageDraw

    WIDTH, HEIGHT = 3200, 1800
    BOX_SIZE = 10
    X_DIM, Y_DIM = (int)(WIDTH / BOX_SIZE), (int)(HEIGHT / BOX_SIZE)

    COLORS = [
        '#ffbe29',
        '#8d153a',
        '#eb7400',
        '#00534e',
        # '#000000',
    ]

    img = Image.new(mode="RGB", size=(X_DIM * BOX_SIZE, Y_DIM * BOX_SIZE))
    draw = ImageDraw.Draw(img)
    for i_x in range(0, X_DIM):
        x = i_x * BOX_SIZE

        for i_y in range(0, Y_DIM):
            y = i_y * BOX_SIZE

            shape = [(x, y), (x + BOX_SIZE, y + BOX_SIZE)]
            h = 120 * (i_x % 3)
            color = COLORS[random.randint(0, len(COLORS) - 1)]
            draw.rectangle(
                shape,
                fill=color,
            )
    img.show()
