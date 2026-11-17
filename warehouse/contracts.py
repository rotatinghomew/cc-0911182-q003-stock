from .checks import text, number, moment


def normalize(table,original):
    row=dict(original)
    for field,value in row.items():
        if field in {'quantity','pack_size'}:
            row[field]=number(value,table!='movements')
        elif field.endswith('_at'):
            row[field]=moment(value)
        else:
            text(value)
    if table=='products' and float(row['pack_size'])<=0:
        raise ValueError('包装数量应大于零')
    if table=='movements' and row['unit'] not in {'piece','box'}:
        raise ValueError('未知数量单位')
    if table=='arrivals' and row['disposition'] not in {'accepted','damaged','lost'}:
        raise ValueError('验收处置无效')
    if table=='transfers' and row['source']==row['destination']:
        raise ValueError('调入调出仓不能相同')
    return row
