#coding=utf-8;

# 导入xlrd 模块  这个是 读模块
import xlrd

# 导入xlwt 模块  这个是写的模块
import xlwt


# 1 文件读的部分
# 指定一个路径 /Users/xunli/Desktop/PyPath/1.xlsx
xls_file_path = "/Users/xunli/Desktop/PyPath/1.xlsx";
# 获取excel 对象
book = xlrd.open_workbook(xls_file_path);
# 获取sheet 对象 获取第二个sheet的名字
sheet_name = book.sheet_names()[2];

# 也可以直接通过sheet 的名字直接获取sheet 对象
sheet1 = book.sheet_by_name("handsome");
# 通过sheet 索引获取sheet 对象
sheet2 = book.sheet_by_index(0)
# 获取总的 行数
nrows = sheet1.nrows;
# 获取总的 列数
ncols = sheet1.ncols;

# 获取指定 行  和 列的值 返回对象为一个值列表
row_data = sheet1.row_values(0);

col_data = sheet1.col_values(0);


# 通过cell的位置坐标获取指定cell 的值 就死代表  0 行  1 列
cell_value1 = sheet1.cell_value(0,1);
#  这个是还附加出了 值的类型 例如: number:1212.0
cell_value2 = sheet1.cell(0,1);

print(cell_value2);



# 文件写的部分
# 创建一个workbook 对象
wbk = xlwt.Workbook(encoding='utf-8',style_compression=0);
# 新建一个sheet 进行写入操作 cell_overwrite_ok 参数用于确认同一个cell 是否可以重新设置值
sheet = wbk.add_sheet('fourth',cell_overwrite_ok=True);

# 进行写入操作
sheet.write(0,1,"第0行第1列写入的数据");

# 进行重写
sheet.write(0,1,"第0行第1列第二次被重写的值");

# 创建一个样式
style = xlwt.XFStyle();
font = xlwt.Font();
font.name = "Times New Roman";
font.bold = True;
style.font = font;

# 写入样式
sheet.write(1,1,'新版的样式',style);



wbk.save('/Users/xunli/Desktop/PyPath/2.xlsx');



