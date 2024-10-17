import pandas as pd
from aqdefreader.file import DfqFile
from aqdefreader.operations import read_dfq_file

# 假设你已经有了一个函数来读取文件并返回DfqFile对象
# 这里我们直接使用read_dfq_file函数
dfq_file = read_dfq_file(r'RE/240506184740.DFQ')

# 初始化一个空的DataFrame来存储所有特性和测量值
all_measurements_df = pd.DataFrame()

# 初始化一个空的DataFrame来存储不合格的结果
不合格结果 = []

# 遍历文件中的每个部分
for part_index, part in enumerate(dfq_file.get_parts()):
    print(f"Processing Part {part_index + 1}:")
    # 遍历部分中的每个特性
    for characteristic_index, characteristic in enumerate(part.get_characteristics()):
        # 获取特性的名称
        characteristic_name = characteristic.get_data("K2002")
        
        # 获取上公差和下公差，如果不存在则设置为None
        upper_tolerance_str = characteristic.get_data("K2111")
        lower_tolerance_str = characteristic.get_data("K2110")
        
        # 尝试将公差字符串转换为浮点数，如果失败则设置为None
        upper_tolerance = None
        lower_tolerance = None
        
        if upper_tolerance_str is not None:
            try:
                upper_tolerance = float(upper_tolerance_str)
            except ValueError:
                print(f"Warning: Upper tolerance value '{upper_tolerance_str}' cannot be converted to float.")
        
        if lower_tolerance_str is not None:
            try:
                lower_tolerance = float(lower_tolerance_str)
            except ValueError:
                print(f"Warning: Lower tolerance value '{lower_tolerance_str}' cannot be converted to float.")
        
        # 如果上公差或下公差不存在，则跳过这个特性的处理
        if upper_tolerance is None or lower_tolerance is None:
            print(f"Skipping characteristic {characteristic_index + 1} due to missing tolerance data.")
            continue

        # 获取特性的测量值
        measurements = characteristic.get_measurements()
        
        # 将测量值转换为DataFrame
        measurements_df = pd.DataFrame(
            [measurement.as_value_dictionary() for measurement in measurements],
            columns=['datetime', 'value']
        )
        
        # 添加特性名称和公差作为新列
        measurements_df['characteristic_name'] = characteristic_name
        measurements_df['upper_tolerance'] = upper_tolerance
        measurements_df['lower_tolerance'] = lower_tolerance
        
        # 检查每个测量值是否在公差内
        measurements_df['is_within_tolerance'] = measurements_df.apply(
            lambda row: lower_tolerance <= row['value'] <= upper_tolerance if row['value'] is not None else False,
            axis=1
        )
        
        # 将测量值DataFrame追加到总的DataFrame中
        all_measurements_df = pd.concat([all_measurements_df, measurements_df], ignore_index=True)

        # 检查是否有不合格的测量值
        if (measurements_df['is_within_tolerance'] == False).any():
            # 获取不合格的测量值
            non_conforming_measurements = measurements_df[measurements_df['is_within_tolerance'] == False]
            for index, row in non_conforming_measurements.iterrows():
                不合格结果.append({
                    'characteristic_name': row['characteristic_name'],
                    'datetime': row['datetime'],
                    'value': row['value'],
                    'upper_tolerance': row['upper_tolerance'],
                    'lower_tolerance': row['lower_tolerance']
                })

# 显示所有测量值的DataFrame
print(all_measurements_df.head())

# 如果有不合格的结果，显示它们
if 不合格结果:
    print("不合格结果：")
    for result in 不合格结果:
        print(f"特性名称：{result['characteristic_name']}, 测量时间：{result['datetime']}, 测量值：{result['value']}, 上公差：{result['upper_tolerance']}, 下公差：{result['lower_tolerance']}")
else:
    print("所有测量值均合格。")