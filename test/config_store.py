from dataclasses import dataclass
from dag_generator import cs

@dataclass
class SQLToCsv:
    source_table: str 
    sql_script: str
    
@dataclass
class S3Upload:
    bucket: str    


cs.store(group='action',name='SQLToCsv',node=SQLToCsv)
cs.store(group='s3',name='S3Upload',node=S3Upload)

