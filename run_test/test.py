from ultralytics import YOLO 
LOOP = 10
def main():
    model = YOLO("/home/user/ros2_ws/src/run_test/run_test/best.pt")
    for i in range(LOOP):

        results = model(f"/home/user/ros2_ws/src/run_test/run_test/image{i}.png",save=True)

        for result in results:
            xywhr = result.obb.xywhr  # center-x, center-y, width, height, angle (radians)
            xyxyxyxy = result.obb.xyxyxyxy  # polygon format with 4-points
            names = [result.names[cls.item()] for cls in result.obb.cls.int()]  # class name of each box
            confs = result.obb.conf  # confidence score of each box


if __name__ == "__main__":
    main()