import os
import yaml

class LoadYaml:
    def __init__(self, filename='info.yaml'):
        self.param_dir = os.path.join(
            os.path.dirname(__file__),
            '..',
            'params'
        )
        self.yamlfile = os.path.join(
            self.param_dir,
            filename
        )
        self.data = self.load_yaml()

    def load_yaml(self):
        if not os.path.exists(self.yamlfile):
            raise FileNotFoundError(f"YAML file not found: {self.yamlfile}")

        with open(self.yamlfile, 'r', encoding='utf-8') as file:
            try:
                data = yaml.safe_load(file)
                return data
            except yaml.YAMLError as exc:
                print(f"Error loading YAML file: {exc}")
                return None

    def get_image_data(self, image_name):
        # 指定されたイメージデータを取得
        if self.data:
            return self.data.get(image_name, {})
        return {}

if __name__ == "__main__":
    load = LoadYaml()  # info.yaml を読み込む
    image_data = load.get_image_data('image_01')

    if image_data:
        print("Image data loaded successfully:")
        print(image_data)
    else:
        print("Failed to load image data.")
