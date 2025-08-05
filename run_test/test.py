from ultralytics import YOLO 
LOOP = 14
def main():
    model = YOLO("/home/user/ros2_ws/src/run_test/run_test/sikitumeta_best.pt")
    output_text = ""
    output_dir = ""
    for i in range(LOOP):
        
        results = model(f"/home/user/ros2_ws/src/run_test/run_test/image{i}.png",save=True)
        # for result in results:
            # xywhr = result.obb.xywhr  # center-x, center-y, width, height, angle (radians)
            # xyxyxyxy = result.obb.xyxyxyxy  # polygon format with 4-points
            # names = [result.names[cls.item()] for cls in result.obb.cls.int()]  # class name of each box
            # confs = result.obb.conf  # confidence score of each box
        obb_boxes = results[0].obb
        num_boxes = obb_boxes.xywhr.shape[0]
        print(f"{i}枚目の検出したバウンディングボックス:{num_boxes}")
        
        output_text += f"image{i},{num_boxes}\n"
        output_dir = results[0].save_dir

    with open(f"{output_dir}/boxes.txt", "w") as txt:
        txt.write(output_text)

if __name__ == "__main__":
    main()
