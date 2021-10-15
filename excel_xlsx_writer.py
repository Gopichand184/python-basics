import xlsxwriter
import pandas as pd
import glob
from datetime import datetime


def initialize_global_variables():

    global sheet_flag_base
    global sheet_flag_scenario
    global row_count_base
    global column_count_base
    global row_count_scenario
    global column_count_scenario
    global excel_sheet_type
    global country_count_base
    global country_count_scenario
    global index_column_base
    global index_column_scenario
    
    
    sheet_flag_base = 0
    sheet_flag_scenario = 0
    row_count_base = 4
    column_count_base = 0
    row_count_scenario = 4
    column_count_scenario = 0
    excel_sheet_type = None
    country_count_base = -1
    country_count_scenario = -1
    index_column_base = 4
    index_column_scenario = 4


def write_first_column_header(workbook, worksheet):

    top_border = workbook.add_format()
    top_border.set_top(1)
    worksheet.write(1, 0, 'Sensitivity', top_border)
    worksheet.write(2, 0, 'Calculation Date')
    worksheet.write(3, 0, 'Month\Currency')

def sub_header_format(workbook):

    sub_header_format_fmt = workbook.add_format()
    sub_header_format_fmt.set_bold()
    sub_header_format_fmt.set_align('center')
    sub_header_format_fmt.set_text_wrap()
    sub_header_format_fmt.bg_color = '#D3D3D3'
    return sub_header_format_fmt

def sub_header_date_format(workbook):

    sub_header_format_date_fmt = workbook.add_format()
    sub_header_format_date_fmt.set_bold()
    sub_header_format_date_fmt.bg_color = '#D3D3D3'
    sub_header_format_date_fmt.set_align('center')
    return sub_header_format_date_fmt

def main_header_format(workbook):

    main_header_format_fmt = workbook.add_format()
    main_header_format_fmt.set_bold()
    main_header_format_fmt.set_valign('vcenter')
    main_header_format_fmt.set_align('center')
    main_header_format_fmt.set_text_wrap()
    main_header_format_fmt.set_bg_color('#D3D3D3')
    main_header_format_fmt.set_bottom(1)
    return main_header_format_fmt

def record_format(workbook):
 
    record_format_fmt = workbook.add_format()
    record_format_fmt.set_align('center')
    record_format_fmt.set_text_wrap()
    record_format_fmt.set_bg_color('#D3D3D3')
    return record_format_fmt

## Sensitivity
## Calculation Date
## Currency
def write_sub_headers(workbook, worksheet, column_count, sensitivity, valuation_date, currency):
    
    sub_header_format1 = sub_header_format(workbook)
    sub_header_format2 = sub_header_format(workbook)
    sub_header_format2.set_right(1)

    worksheet.write(1, column_count + 1, sensitivity, sub_header_format1)
    worksheet.write(1, column_count + 2, sensitivity, sub_header_format1)
    worksheet.write(1, column_count + 3, sensitivity, sub_header_format1)
    worksheet.write(1, column_count + 4, sensitivity, sub_header_format2)
    
    
    
    worksheet.write(3, column_count + 1, currency, sub_header_format1)
    worksheet.write(3, column_count + 2, currency, sub_header_format1)
    worksheet.write(3, column_count + 3, currency, sub_header_format1)
    worksheet.write(3, column_count + 4, currency, sub_header_format2)

    sub_header_date_format1 = sub_header_date_format(workbook)
    sub_header_date_format2 = sub_header_date_format(workbook)
    sub_header_date_format2.set_right(1)

    sub_header_date_format1.set_num_format(';;; "{}" '.format(valuation_date[5:]))
    sub_header_date_format2.set_num_format(';;; "{}" '.format(valuation_date[5:]))
    
    worksheet.write(2, column_count + 1, " " + valuation_date+ " ", sub_header_date_format1)
    worksheet.write(2, column_count + 2, " " + valuation_date+ " ", sub_header_date_format1)
    worksheet.write(2, column_count + 3, " " + valuation_date+ " ", sub_header_date_format1)
    worksheet.write(2, column_count + 4, " " + valuation_date+ " ", sub_header_date_format2)

        
## ,Discount Facotr,Annualized Spot Rates,Annualized Forward Rates,Par Rates, BEY
def write_main_headers(workbook, worksheet, country_name):

    global column_count
    global column_count_scenario
    global excel_sheet_type

    discount_factor_header = country_name + " " + "Discount Factor"
    annualised_spot_rates_header = country_name + " " + "Annualised Spot Rates"
    annualised_forward_rates_header = country_name + " " + "Annualised Forward Rates"
    par_rates_header = country_name + " " + "Par Rates, BEY"

    if excel_sheet_type == "BASE_ALL":
        column_number = column_count_base
    elif excel_sheet_type == "SENSITIVITY_ALL":
        column_number = column_count_scenario
    
    worksheet.set_row(0, 80)
    worksheet.set_column(1, column_number + 4, 12)
    worksheet.set_column('A:A', 20)

    main_header_format1 = main_header_format(workbook)
    main_header_format2 = main_header_format(workbook)
    main_header_format2.set_right(1)
    worksheet.write(0, column_number + 1, discount_factor_header, main_header_format1)
    worksheet.write(0, column_number + 2, annualised_spot_rates_header, main_header_format1)
    worksheet.write(0, column_number + 3, annualised_forward_rates_header, main_header_format1)
    worksheet.write(0, column_number + 4, par_rates_header, main_header_format2)


def write_record(workbook, worksheet,
                discount_factor, annualized_spot_rates,
                annualized_forward_rates, par_rate,
                months,
                row_number, column_number):
    
    record_format1 = record_format(workbook)
    record_format1.set_num_format('0.000#')
    record_format2 = record_format(workbook)
    record_format2.set_num_format('0.00#"%"')
    record_format3 = record_format(workbook)
    record_format3.set_num_format('0.00#"%"')
    record_format3.set_right(1)
    
    worksheet.write(row_number, column_number+1, discount_factor, record_format1)
    worksheet.write(row_number, column_number+2, annualized_spot_rates, record_format2)
    worksheet.write(row_number, column_number+3, annualized_forward_rates, record_format2)
    worksheet.write(row_number, column_number+4, par_rate, record_format3)
    worksheet.write(row_number, 0, months)
    

def extract_data(workbook, df, sheet_type):
    ## Argument - excel_sheet_type
    ## Base means single sheet excel with all the rates of the all the country currency
    ## Scenario means single shrret excel with multiple rates of the single country currency

    header_write_flag = 0

    global sheet_flag_base
    global sheet_flag_scenario
    global excel_sheet_type
    global country_count_base
    global country_count_scenario
    global column_count_base
    global column_count_scenario
    global row_count_base
    global row_count_scenario
    global worksheet

    previous_sensitivity = None
    excel_sheet_type = sheet_type
    sheet_flag_scenario = 0

    for record in df.itertuples():

        country_name = getattr(record, 'CountryCd')
        sensitivity = getattr(record, 'ScenarioName')
        valuation_date = getattr(record, 'ValuationDate')
        currency = getattr(record, 'CurrencyCd')
        discount_factor = getattr(record, 'DiscountRate')
        annualized_spot_rates = getattr(record, 'AnnualizedSpotRate')
        annualized_forward_rates = getattr(record, 'AnnualizedForwardRate')
        par_rate = getattr(record, 'ParRate')
        index_column = getattr(record, 'TenorInMonths')

        if excel_sheet_type == "BASE_ALL":
            
            ## Sheet flag is used to populate the valutaion date as sheet name for base excel sheet
            if sheet_flag_base == 0:
                sheet_flag_base = 1
                worksheet = workbook.add_worksheet(valuation_date.replace("/", "-"))
                write_first_column_header(workbook, worksheet)
            
            ## Header flag is used to populate header once when we read the records
            if header_write_flag == 0:
                row_count_base = 4
                header_write_flag = 1
                country_count_base += 1
                column_count_base = country_count_base * 4
                write_main_headers(workbook, worksheet, country_name)
                write_sub_headers(workbook, worksheet,
                                  column_count_base, sensitivity, 
                                  valuation_date.replace("-", "/"), currency)
                write_record(workbook, worksheet,
                             discount_factor, annualized_spot_rates, 
                             annualized_forward_rates, par_rate, 
                             index_column, 
                             row_count_base, column_count_base)
            else:
                row_count_base += 1
                write_record(workbook, worksheet,
                             discount_factor, annualized_spot_rates, 
                             annualized_forward_rates, par_rate, 
                             index_column, 
                             row_count_base, column_count_base)
                
        elif excel_sheet_type == "SENSITIVITY_ALL":
            
            if previous_sensitivity is None:
                previous_sensitivity = sensitivity
            elif previous_sensitivity != sensitivity:
                previous_sensitivity = sensitivity
                row_count_scenario = 3
                country_count_scenario += 1
                column_count_scenario = country_count_scenario * 4
                write_main_headers(workbook, worksheet, country_name)
                write_sub_headers(workbook, worksheet,
                                  column_count_scenario, sensitivity,
                                  valuation_date.replace("-", "/"), currency)
            ## Sheet flag is used to populate the valutaion date as sheet name for base excel sheet
            if sheet_flag_scenario == 0:
                sheet_flag_scenario = 1
                country_count_scenario = -1
                worksheet = workbook.add_worksheet(currency)
                write_first_column_header(workbook, worksheet)

            ## Header flag is used to populate header once when we read the records
            if header_write_flag == 0:

                row_count_scenario = 4
                header_write_flag = 1
                country_count_scenario += 1
                column_count_scenario = country_count_scenario * 4
                write_main_headers(workbook, worksheet, country_name)
                write_sub_headers(workbook, worksheet,
                                  column_count_scenario, sensitivity, 
                                  valuation_date.replace("-", "/"), currency)
                write_record(workbook, worksheet,
                             discount_factor, annualized_spot_rates, 
                             annualized_forward_rates, par_rate, 
                             index_column, 
                             row_count_scenario, column_count_scenario)
            else:
                row_count_scenario += 1
                write_record(workbook, worksheet,
                             discount_factor, annualized_spot_rates, 
                             annualized_forward_rates, par_rate, 
                             index_column, 
                             row_count_scenario, column_count_scenario)


## Open excel for writing
## Read from data frame and pass it to the function extract_data
workbook = xlsxwriter.Workbook('Rates.xlsx')
initialize_global_variables()
for file_name in glob.glob("*.csv"):
    df = pd.read_csv(file_name, sep = ",")
    extract_data(workbook, df, "SENSITIVITY_ALL")
workbook.close()
