def actual_value_extraction(filepath):
        try:
            with open(filepath, "rb") as f:
                lines = f.read().decode("ascii", errors="replace").splitlines()#line是一个列表 索引值对应每一行，空行视为一行
                target_string=lines[214]
            ist_mass=(target_string[0:7],target_string[30:39],target_string[40:47],target_string[48:55],target_string[56:63],target_string[64:71],target_string[72:79],target_string[80:87],target_string[88:95],target_string[97:105],target_string[106:113],target_string[114:121])
            return ist_mass
        except IndexError:
                       print("文件内容不符合预期，无法找到目标行。")
def 
# if __name__=="__main__":
#         dfq_file=input('请在此处粘贴目标文件路径')
#         print(actual_value_extraction(dfq_file))