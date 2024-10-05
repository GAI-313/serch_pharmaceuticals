# serch_pharmaceuticals

## usage
 Launch in venv. after install this package
```
pip install -e .
```
 You can execute to this command
```
sp_main
```

If you edit profile, Edit to this in 'src\serch_pharmaceuticals.py`
```python
RATE = 2                        # 選択回数
VAL_MIN = 36                    # 開始番号
VAL_MAX = 40                    # 終了番号
PROJ_NAME = 'Sample'    # データベース名
```
- RATE : Rate of ask the quest
- VAL_MIN and VAL_MAX<br>
    - Ex1: 1, 12
    - Ex2: 13, 27
    - Ex3: 29, 42
    - Ex4: 43, 56
- PROJ_NAME: Data file name of current exam task :Example . Examer name...

## Data base
 Exam result data type is `.csv`. You can check via Exel.

|**Image name**|**Target name**|**Success Clicked**|**Interval**|**Clicked Pose (Pixel2D)**|
|:---:|:---:|:---:|:---:|:---:|
|image_01|アムリキド|True|00.10.230|[270,300]|
|image_01|アレグラ|False|00.10.230|[270,300]|
