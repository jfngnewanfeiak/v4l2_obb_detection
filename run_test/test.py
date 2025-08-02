from ultralytics import YOLO 
LOOP = 14
def main():
    model = YOLO("/home/user/ros2_ws/src/run_test/run_test/kougenn_random_x_best.pt")
    for i in range(LOOP):

        results = model(f"/home/user/ros2_ws/src/run_test/run_test/image{i}.png",save=True)

        for result in results:
            # xywhr = result.obb.xywhr  # center-x, center-y, width, height, angle (radians)
            # xyxyxyxy = result.obb.xyxyxyxy  # polygon format with 4-points
            # names = [result.names[cls.item()] for cls in result.obb.cls.int()]  # class name of each box
            # confs = result.obb.conf  # confidence score of each box
            pass
        print(f"{i}枚目の検出したバウンディングボックス:{len(results)}")

if __name__ == "__main__":
    main()
