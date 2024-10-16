from aqdefreader import operations as ao
from aqdefreader import file
from aqdefreader.operations import read_dfq_file, create_column_dataframe
from aqdefreader.file import DfqFile
aa=ao.read_dfq_file(r'C:\Users\David\Desktop\messen-monitoring\RE\240506184740.DFQ')
df=create_column_dataframe(aa, part_index=0, group_by_date=False)
print(df)