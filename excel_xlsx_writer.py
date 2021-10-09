import xlsxwriter
import pandas as pd

## These columns represent the headers in the csv file
column_names = ["Country Name", "Sensitivity", "Date", "Currency",  "Discount Factor", "Annualised Spot Rates", "Annualised Forward Rates", "Par Rates BEY"]

## Excel file name
workbook = xlsxwriter.Workbook('final.xlsx')

## Main header "Discount Factor", "Annualised Spot Rates", "Annualised Forward Rates", "Par Rates BEY"
main_header_format = workbook.add_format({'bold' : True, 'valign' : 'vcenter', 'align' : 'center', 'text_wrap' : True, 'bg_color' : '#D3D3D3'})
## Sub headers "Sensitivity", "Date", "Currency"
sub_header = workbook.add_format({'bold' : True, 'align' : 'center', 'text_wrap' : True, 'bg_color' : '#D3D3D3'})

## Border formatting for the headers first border horizontal top border for "Sensitivity"
border_header_horizontal = workbook.add_format()
border_header_horizontal.set_bold()
border_header_horizontal.set_align('center')
border_header_horizontal.set_text_wrap()
border_header_horizontal.bg_color = '#D3D3D3'
border_header_horizontal.set_top(1)

## Border formatting for header vertical border right border for "Par Rates BEY"
border_header_vertical_header = workbook.add_format()
border_header_vertical_header.set_bold()
border_header_vertical_header.set_valign('vcenter')
border_header_vertical_header.set_align('center')
border_header_vertical_header.set_text_wrap()
border_header_vertical_header.set_right(1)
border_header_vertical_header.bg_color ='#D3D3D3'


## Border formatting for sub header vertical border right border for "Sensitivity", "Date", "Currency",
border_sub_header_vertical_header = workbook.add_format()
border_sub_header_vertical_header.set_bold()
border_sub_header_vertical_header.set_align('center')
border_sub_header_vertical_header.set_text_wrap()
border_sub_header_vertical_header.set_right(1)
border_sub_header_vertical_header.bg_color = '#D3D3D3'


## Border formatting for sub headers horizontal border and vertical border for last sensitivity column
border_sub_header_horizontal_vertical_header= workbook.add_format()
border_sub_header_horizontal_vertical_header.set_bold()
border_sub_header_horizontal_vertical_header.set_align('center')
border_sub_header_horizontal_vertical_header.set_text_wrap()
border_sub_header_horizontal_vertical_header.set_right(1)
border_sub_header_horizontal_vertical_header.set_top(1)
border_sub_header_horizontal_vertical_header.bg_color = '#D3D3D3'


row_number = 0
column_number = 0

previous_country = None
country_count = 0

## used to populate the record number on the first column
index = 0


## Here # represents round off value
## format for the column "Annualised Spot Rates", "Annualised Forward Rates"
percentage_value_precision = workbook.add_format()
percentage_value_precision.set_num_format('0.00#"%"')
percentage_value_precision.bg_color = '#D3D3D3'
percentage_value_precision.set_align('center')

## Here # represents round off value
## format for the column "Par Rates BEY"
percentage_value_precision_border = workbook.add_format()
percentage_value_precision_border.set_num_format('0.00#"%"')
percentage_value_precision_border.set_right(1)
percentage_value_precision_border.bg_color = '#D3D3D3'
percentage_value_precision_border.set_align('center')

## Here # represents round off value
## format for the column "Discount Factor"
record_value_precision = workbook.add_format()
record_value_precision.set_num_format('0.000#')
record_value_precision.bg_color = '#D3D3D3'
record_value_precision.set_align('center')

## read from csv file as data frames
df = pd.read_csv("percentage.csv", sep = ",")

for outer_index, row_data in df.iterrows():
    
    present_country_name = row_data[0]
    sensitivity = row_data[1]
    date = row_data[2]
    currency = row_data[3]
    discount_factor = row_data[4]
    annualised_spot_rates = row_data[5]
    annualised_forward_rates = row_data[6]
    par_rates_bey = row_data[7]
    

    ## This if condition executes only for the first record
    if previous_country is None:
        
        ## Dynamic poplation of date to the sheet name
        worksheet = workbook.add_worksheet(date.replace("/", "-"))

        ## Hard coded first column values
        top_border = workbook.add_format()
        top_border.set_top(1)
        worksheet.write(1, 0, 'Sensitivity', top_border)
        worksheet.write(2, 0, 'Calculation Date')
        worksheet.write(3, 0, 'Currency')
        
        previous_country = present_country_name

        row_number = 0
        
        ## 4 Top Headers Data about Rates
        ##  "Discount Factor", "Annualised Spot Rates", "Annualised Forward Rates", "Par Rates BEY"
        worksheet.write(row_number, column_number+1, present_country_name + " " + column_names[4], main_header_format)
        worksheet.write(row_number, column_number+2, present_country_name + " " + column_names[5], main_header_format)
        worksheet.write(row_number, column_number+3, present_country_name + " " + column_names[6], main_header_format)
        worksheet.write(row_number, column_number+4, present_country_name + " " + column_names[7], border_header_vertical_header)

        
        ## Sensitivity
        worksheet.write(row_number+1, column_number+1, sensitivity, border_header_horizontal)
        worksheet.write(row_number+1, column_number+2, sensitivity, border_header_horizontal)
        worksheet.write(row_number+1, column_number+3, sensitivity, border_header_horizontal)
        worksheet.write(row_number+1, column_number+4, sensitivity, border_sub_header_horizontal_vertical_header)
        ## Date
        worksheet.write(row_number+2, column_number+1, date, sub_header)
        worksheet.write(row_number+2, column_number+2, date, sub_header)
        worksheet.write(row_number+2, column_number+3, date, sub_header)
        worksheet.write(row_number+2, column_number+4, date, border_sub_header_vertical_header)
        ##Currency
        worksheet.write(row_number+3, column_number+1, currency, sub_header)
        worksheet.write(row_number+3, column_number+2, currency, sub_header)
        worksheet.write(row_number+3, column_number+3, currency, sub_header)
        worksheet.write(row_number+3, column_number+4, currency, border_sub_header_vertical_header)
        
        row_number = 4
        
        ## Actual Rates Data
        worksheet.write(row_number, column_number+1, discount_factor, record_value_precision)
        worksheet.write(row_number, column_number+2, annualised_spot_rates, percentage_value_precision)
        worksheet.write(row_number, column_number+3, annualised_forward_rates, percentage_value_precision)
        worksheet.write(row_number, column_number+4, par_rates_bey, percentage_value_precision_border)

        column_number = 1
        index += 1

    ## When ever there is change in the country name we need to populate the records in next adjacent columns
    elif previous_country != present_country_name:

        row_number = 0
        country_count += 1
        column_number = country_count * 4 + 1
        previous_country = present_country_name
        ## 4 Top Headers Data about Rates
        ##  "Discount Factor", "Annualised Spot Rates", "Annualised Forward Rates", "Par Rates BEY"
        
        worksheet.write(row_number, column_number, present_country_name + " " + column_names[4], main_header_format)
        worksheet.write(row_number, column_number+1, present_country_name + " " + column_names[5], main_header_format)
        worksheet.write(row_number, column_number+2, present_country_name + " " + column_names[6], main_header_format)
        worksheet.write(row_number, column_number+3, present_country_name + " " + column_names[7], border_header_vertical_header)
        ## Sensitivity
        worksheet.write(row_number+1, column_number, sensitivity, border_header_horizontal)
        worksheet.write(row_number+1, column_number+1, sensitivity, border_header_horizontal)
        worksheet.write(row_number+1, column_number+2, sensitivity, border_header_horizontal)
        worksheet.write(row_number+1, column_number+3, sensitivity, border_sub_header_horizontal_vertical_header)
        ## Date
        worksheet.write(row_number+2, column_number, date, sub_header)
        worksheet.write(row_number+2, column_number+1, date, sub_header)
        worksheet.write(row_number+2, column_number+2, date, sub_header)
        worksheet.write(row_number+2, column_number+3, date, border_sub_header_vertical_header)
        ##Currency
        worksheet.write(row_number+3, column_number, currency, sub_header)
        worksheet.write(row_number+3, column_number+1, currency, sub_header)
        worksheet.write(row_number+3, column_number+2, currency, sub_header)
        worksheet.write(row_number+3, column_number+3, currency, border_sub_header_vertical_header)
        
        row_number = 4
        
        ## Actual Rates Data
        worksheet.write(row_number, column_number, discount_factor, record_value_precision)
        worksheet.write(row_number, column_number+1, annualised_spot_rates, percentage_value_precision)
        worksheet.write(row_number, column_number+2, annualised_forward_rates, percentage_value_precision)
        worksheet.write(row_number, column_number+3, par_rates_bey, percentage_value_precision_border)
        
        index = 0

    else:
        row_number += 1

        ## Actual Rates Data
        worksheet.write(row_number, column_number, discount_factor, record_value_precision)
        worksheet.write(row_number, column_number+1, annualised_spot_rates, percentage_value_precision)
        worksheet.write(row_number, column_number+2, annualised_forward_rates, percentage_value_precision)
        worksheet.write(row_number, column_number+3, par_rates_bey, percentage_value_precision_border)
        index += 1
        
    

    print(row_number, column_number)

##Write Index at last serial number or record number at the first column
for index_value in range(0, index+1):
    worksheet.write(4 + index_value, 0, index_value + 1)

## column is used to set the width of the cell and row is used to set the height of the cell
worksheet.set_column(1, column_number + 4, 12)
worksheet.set_column('A:A', 20)
worksheet.set_row(0, 80)


workbook.close()