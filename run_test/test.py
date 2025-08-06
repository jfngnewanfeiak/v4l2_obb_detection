from ultralytics import YOLO 
from PIL import Image

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
    
    del model
    del results
    
    
    with open(f"{output_dir}/boxes.txt", "r") as read_txt:
            data = read_txt.readlines()

    for i in range(LOOP):
        img = Image.open(f'{output_dir}/image{i}.jpg')

        img.show()

        count_box = int(input("数えたやつを入力"))

        split_data = data[i].split(',')
        back_slash_idx = data[i].find('\n')
        data[i] = data[i][:back_slash_idx] + f",{count_box},{count_box / int(split_data[1])}\n"
    
    with open(f"{output_dir}/result.txt","w") as result_txt:
        output_text = "".join(data)
        result_txt.write(output_text)


if __name__ == "__main__":
    main()
