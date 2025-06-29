import json
import mysql.connector
 
# Load the raw property data from JSON
with open('../data/fake_property_data.json') as f:
    data = json.load(f)
 
# Connect to MySQL database using updated Docker credentials
conn = mysql.connector.connect(
    host='localhost',
    user='db_user',
    password='6equj5_db_user',
    database='home_db'
)
cursor = conn.cursor()
 
for entry in data:
    # Insert into properties table
    props = (
        entry.get('Property_Title'),
        entry.get('Address'),
        entry.get('Street_Address'),
        entry.get('City'),
        entry.get('State'),
        entry.get('Zip'),
        entry.get('Reviewed_Status'),
        entry.get('Most_Recent_Status'),
        entry.get('Source'),
        entry.get('Market'),
        entry.get('Occupancy'),
        entry.get('Flood'),
        entry.get('Property_Type'),
        entry.get('Highway'),
        entry.get('Train'),
        entry.get('Tax_Rate'),
        entry.get('SQFT_Basement'),
        entry.get('HTW'),
        entry.get('Pool'),
        entry.get('Commercial'),
        entry.get('Water'),
        entry.get('Sewage'),
        entry.get('Year_Built'),
        entry.get('SQFT_MU'),
        entry.get('SQFT_Total'),
        entry.get('Parking'),
        entry.get('Bed'),
        entry.get('Bath'),
        entry.get('BasementYesNo'),
        entry.get('Layout'),
        entry.get('Net_Yield'),
        entry.get('IRR'),
        entry.get('Rent_Restricted'),
        entry.get('Neighborhood_Rating'),
        entry.get('Latitude'),
        entry.get('Longitude'),
        entry.get('Subdivision'),
        entry.get('Taxes'),
        entry.get('Selling_Reason'),
        entry.get('Seller_Retained_Broker'),
        entry.get('Final_Reviewer'),
        entry.get('School_Average')
    )
 
    cursor.execute("""
        INSERT INTO properties (
            property_title, address, street_address, city, state, zip, reviewed_status, most_recent_status,
            source, market, occupancy, flood, property_type, highway, train, tax_rate, sqft_basement, htw,
            pool, commercial, water, sewage, year_built, sqft_mu, sqft_total, parking, bed, bath,
            basement_yes_no, layout, net_yield, irr, rent_restricted, neighborhood_rating, latitude, longitude,
            subdivision, taxes, selling_reason, seller_retained_broker, final_reviewer, school_average
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, props)
    property_id = cursor.lastrowid
 
    # Insert into valuations
    for v in entry.get('Valuation', []):
        cursor.execute("""
            INSERT INTO valuations (
                property_id, list_price, previous_rent, arv, zestimate, expected_rent, rent_zestimate,
                low_fmr, high_fmr, redfin_value
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            property_id,
            v.get('List_Price'), v.get('Previous_Rent'), v.get('ARV'),
            v.get('Zestimate'), v.get('Expected_Rent'), v.get('Rent_Zestimate'),
            v.get('Low_FMR'), v.get('High_FMR'), v.get('Redfin_Value')
        ))
 
    # Insert into HOA
    for h in entry.get('HOA', []):
        cursor.execute("""
            INSERT INTO hoa (property_id, hoa, hoa_flag)
            VALUES (%s, %s, %s)
        """, (property_id, h.get('HOA'), h.get('HOA_Flag')))
 
    # Insert into rehab
    for r in entry.get('Rehab', []):
        cursor.execute("""
            INSERT INTO rehab (
                property_id, underwriting_rehab, rehab_calculation, paint,
                flooring_flag, foundation_flag, roof_flag, hvac_flag,
                kitchen_flag, bathroom_flag, appliances_flag, windows_flag,
                landscaping_flag, trashout_flag
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            property_id,
            r.get('Underwriting_Rehab'), r.get('Rehab_Calculation'), r.get('Paint'),
            r.get('Flooring_Flag'), r.get('Foundation_Flag'), r.get('Roof_Flag'), r.get('HVAC_Flag'),
            r.get('Kitchen_Flag'), r.get('Bathroom_Flag'), r.get('Appliances_Flag'), r.get('Windows_Flag'),
            r.get('Landscaping_Flag'), r.get('Trashout_Flag')
        ))
 
# Finalize inserts
conn.commit()
cursor.close()
conn.close()
 
print("ETL completed successfully.")
