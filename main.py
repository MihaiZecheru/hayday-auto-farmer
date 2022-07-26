import dataclasses, sys, time, random
import pyautogui as p


@dataclasses.dataclass
class Point(object):
    x: int
    y: int


def sell_wheat():
    time.sleep(3)
    market = p.locateOnScreen("./static/market.png", confidence=0.7)
    if market is None: return
    p.moveTo(market.left + (market.width / 2), market.top + (market.height / 2), 0.4)
    p.leftClick()

    # place new
    while p.locateOnScreen("./static/market_add_friends_button.png", confidence=0.9) is None:
        # collect sold
        while True:
            sold = p.locateOnScreen("./static/market_sold.png", confidence=0.9)
            if sold is None: break
            p.moveTo(sold.left + (sold.width / 2), sold.top + (sold.height / 2), 0.2)
            p.leftClick()
        while True:
            empty_box = p.locateOnScreen("./static/market_empty_box.png", confidence=0.9)
            if empty_box is None: break
            p.moveTo(empty_box.left + (empty_box.width / 2), empty_box.top + (empty_box.height / 2), 0.2)
            p.leftClick()
            wheat = p.locateOnScreen("./static/market_wheat.png", confidence=0.9)
            if wheat is None:
                silo = p.locateOnScreen("./static/market_silo.png", confidence=0.9)
                p.moveTo(silo.left + (silo.width / 2), silo.top + (silo.height / 2), 0.1)
                p.leftClick()
                time.sleep(0.1)
                wheat = p.locateOnScreen("./static/market_wheat.png", confidence=0.9)
                if wheat is None:
                    time.sleep(0.2)
                    p.keyDown('esc')
                    p.keyUp('esc')
                    time.sleep(0.2)
                    p.keyDown('esc')
                    p.keyUp('esc')
            try:
                p.moveTo(wheat.left + (wheat.width / 2), wheat.top + (wheat.height / 2), 0.1)
            except: return
            p.leftClick()
            while p.locateOnScreen("./static/market_grayed_plus.png", confidence=0.9) is None:
                plus = p.locateOnScreen("./static/market_plus.png", confidence=0.9)
                p.moveTo(plus.left + (plus.width / 2), plus.top + (plus.height / 2), 0.13)
                p.leftClick()
            max_price_button = p.locateOnScreen("./static/market_max_price_button.png", confidence=0.9)
            p.moveTo(max_price_button.left + (max_price_button.width / 2), max_price_button.top + (max_price_button.height / 2), 0.2)
            p.leftClick()
            newspaper = p.locateOnScreen("./static/market_newspaper.png", confidence=0.7)
            if newspaper is not None:
                p.moveTo(newspaper.left + (newspaper.width / 2), newspaper.top + (newspaper.height / 2), 0.13)
                p.leftClick()
            put_on_sale = p.locateOnScreen("./static/market_put_on_sale.png", confidence=0.9)
            p.moveTo(put_on_sale.left + (put_on_sale.width / 2), put_on_sale.top + (put_on_sale.height / 2), 0.13)
            p.leftClick()
        end_of_market = p.locateOnScreen("./static/market_add_friends_button.png", confidence=0.9)
        if end_of_market is not None: break
        box_seperator = p.locateOnScreen("./static/market_box_seperator.png", confidence=0.9)
        p.moveTo(box_seperator.left + (box_seperator.width / 2), box_seperator.top + (box_seperator.height / 2), 0.13)
        p.mouseDown()
        p.moveRel(-300, 0, 0.4)
        p.mouseUp()

    # repeat one more time
    while True:
        empty_box = p.locateOnScreen("./static/market_empty_box.png", confidence=0.9)
        if empty_box is None: break
        p.moveTo(empty_box.left + (empty_box.width / 2), empty_box.top + (empty_box.height / 2), 0.2)
        p.leftClick()
        wheat = p.locateOnScreen("./static/market_wheat.png", confidence=0.9)
        if wheat is None:
            silo = p.locateOnScreen("./static/market_silo.png", confidence=0.9)
            p.moveTo(silo.left + (silo.width / 2), silo.top + (silo.height / 2), 0.1)
            p.leftClick()
            time.sleep(0.1)
            wheat = p.locateOnScreen("./static/market_wheat.png", confidence=0.9)
            if wheat is None:
                time.sleep(0.2)
                p.keyDown('esc')
                p.keyUp('esc')
                time.sleep(0.2)
                p.keyDown('esc')
                p.keyUp('esc')
        p.moveTo(wheat.left + (wheat.width / 2), wheat.top + (wheat.height / 2), 0.1)
        p.leftClick()
        while p.locateOnScreen("./static/market_grayed_plus.png", confidence=0.9) is None:
            plus = p.locateOnScreen("./static/market_plus.png", confidence=0.9)
            p.moveTo(plus.left + (plus.width / 2), plus.top + (plus.height / 2), 0.13)
            p.leftClick()
        max_price_button = p.locateOnScreen("./static/market_max_price_button.png", confidence=0.9)
        p.moveTo(max_price_button.left + (max_price_button.width / 2),
                 max_price_button.top + (max_price_button.height / 2), 0.2)
        p.leftClick()
        newspaper = p.locateOnScreen("./static/market_newspaper.png", confidence=0.7)
        if newspaper is not None:
            p.moveTo(newspaper.left + (newspaper.width / 2), newspaper.top + (newspaper.height / 2), 0.13)
            p.leftClick()
        put_on_sale = p.locateOnScreen("./static/market_put_on_sale.png", confidence=0.9)
        p.moveTo(put_on_sale.left + (put_on_sale.width / 2), put_on_sale.top + (put_on_sale.height / 2), 0.13)
        p.leftClick()

    time.sleep(0.2)
    p.keyDown('esc')
    p.keyUp('esc')

    if p.locateOnScreen("./static/market_sign.png", confidence=0.9) is not None:
        time.sleep(0.2)
        p.keyDown('esc')
        p.keyUp('esc')

                         # all but first      first
def locate_fields(farm: str) -> tuple[list[Point], Point, Point]:
    image = p.locateOnScreen(f"./static/{farm}.png", confidence=0.5)
    if image is None:
        return []

    left, top, width, height = image.left, image.top, image.width, image.height
    row = [Point(227, 32), Point(190, 50), Point(160, 71), Point(130, 83), Point(100, 98)]

    fields = [
        Point(left + row[0].x, top + row[0].y),
        Point(left + row[1].x, top + row[1].y),
        Point(left + row[2].x, top + row[2].y),
        Point(left + row[3].x, top + row[3].y),
        Point(left + row[4].x, top + row[4].y),

        Point(left + row[0].x + 30, top + row[0].y + 18),
        Point(left + row[1].x + 30, top + row[1].y + 18),
        Point(left + row[2].x + 30, top + row[2].y + 18),
        Point(left + row[3].x + 30, top + row[3].y + 18),
        Point(left + row[4].x + 30, top + row[4].y + 18),

        Point(left + row[0].x + 60, top + row[0].y + 36),
        Point(left + row[1].x + 60, top + row[1].y + 36),
        Point(left + row[2].x + 65, top + row[2].y + 33),
        Point(left + row[3].x + 60, top + row[3].y + 36),
        Point(left + row[4].x + 60, top + row[4].y + 36),

        Point(left + row[0].x + 100, top + row[0].y + 50),
        Point(left + row[1].x + 100, top + row[1].y + 50),
        Point(left + row[2].x + 100, top + row[2].y + 50),
        Point(left + row[3].x + 100, top + row[3].y + 50),
        Point(left + row[4].x + 100, top + row[4].y + 50),

        Point(left + row[0].x + 131, top + row[0].y + 67),
        Point(left + row[1].x + 131, top + row[1].y + 67),
        Point(left + row[2].x + 131, top + row[2].y + 67),
        Point(left + row[3].x + 131, top + row[3].y + 67),
        # last slot missing
    ]

    first_field = fields.pop(0)
    last_field = fields.pop(0)
    random.shuffle(fields)
    return (fields, first_field, last_field)


def main(argv):
    time.sleep(1.5)

    if len(argv) != 2:
        print("Usage: python main.py <farmname>")
        return 1

    farm = argv[1]
    if farm not in ["Chrysler", "ChryslerChris3", "ChryslerChris4"]:
        print("<farmname> must be one of the following: Chrysler, ChryslerChris3, ChryslerChris4")
        return 1

    fields, first_field, last_field = locate_fields(farm)

    # image of fields could not be found
    if len(fields) == 0:
        return

    if farm == "ChryslerChris3":
        # place wheat
        p.moveTo(first_field.x, first_field.y, 0.2)
        p.click()
        time.sleep(0.5)
        wheat = p.locateOnScreen("./static/wheat.png", confidence=0.5)
        p.moveTo(wheat.left + (wheat.width / 2), wheat.top + (wheat.height / 2), 0.17)
        p.mouseDown()
        p.moveTo(first_field.x, first_field.y, 0.2)

        for i in range(1, len(fields) - 1):
            p.moveTo(fields[i].x, fields[i].y, 0.16)

        p.moveTo(last_field.x, last_field.y, 0.16)
        time.sleep(1.150)
        p.mouseUp()

        # # click off of the growing wheat to remove the extra menus
        # spot = p.locateOnScreen("./static/spot_near_barn.png", confidence=0.5)
        # p.moveTo(spot.left + (spot.width / 3.7), spot.top + (spot.height / 1.3))
        # time.sleep(0.050)
        # p.click()

    first = True

    while True:
        # wait for wheat to grow
        if first:
            time.sleep(60 * 2 + 5)  # 2:05
            first = False
        else: time.sleep(60 * 2 - 20) # 1:40

        if farm == "ChryslerChris3":
            # collect wheat
            sickle = p.locateOnScreen("./static/sickle.png", confidence=0.9)

            if sickle is None:
                p.moveTo(last_field.x, last_field.y, 0.17)
                time.sleep(0.075)
                p.leftClick()
                time.sleep(1)
                sickle = p.locateOnScreen("./static/sickle.png", confidence=0.9)

            p.moveTo(sickle.left + 30, sickle.top + 10)
            p.mouseDown()

            p.moveTo(first_field.x, first_field.y, 0.2)
            time.sleep(0.050)

            for i in range(1, len(fields) - 1):
                p.moveTo(fields[i].x, fields[i].y, 0.16)

            p.moveTo(last_field.x, last_field.y, 0.16)
            time.sleep(1.150)
            p.mouseUp()

            time.sleep(5)

            # place wheat again
            p.moveTo(first_field.x, first_field.y, 0.2)
            p.click()
            time.sleep(0.5)
            wheat = p.locateOnScreen("./static/wheat.png", confidence=0.5)
            p.moveTo(wheat.left + (wheat.width / 2), wheat.top + (wheat.height / 2), 0.17)
            p.mouseDown()
            p.moveTo(first_field.x, first_field.y, 0.2)

            for i in range(1, len(fields) - 1):
                p.moveTo(fields[i].x, fields[i].y, 0.16)

            p.moveTo(last_field.x, last_field.y, 0.16)
            time.sleep(1.150)
            p.mouseUp()

            # # click off of the growing wheat to remove the extra menus
            # spot = p.locateOnScreen("./static/spot_near_barn.png", confidence=0.5)
            # p.moveTo(spot.left + (spot.width / 3.7), spot.top + (spot.height / 1.3))
            # time.sleep(0.050)
            # p.click()

            # sell wheat
            sell_wheat()

if __name__ == "__main__":
    print("\nTo prepare the program, first align the market's crates with the edge of the screen,"
          "and scroll down so the field is not centered,\n"
          "then click on the top left-most field to allow the game to center the field itself.")
    time.sleep(1.5)
    main(sys.argv)