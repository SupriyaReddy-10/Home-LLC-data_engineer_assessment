-- 1. Main Properties Table
CREATE TABLE properties (
    property_id INT AUTO_INCREMENT PRIMARY KEY,
    property_title TEXT,
    address TEXT,
    street_address TEXT,
    city VARCHAR(100),
    state VARCHAR(10),
    zip VARCHAR(20),
    reviewed_status VARCHAR(50),
    most_recent_status VARCHAR(50),
    source VARCHAR(100),
    market VARCHAR(100),
    occupancy VARCHAR(50),
    flood VARCHAR(100),
    property_type VARCHAR(100),
    highway VARCHAR(100),
    train VARCHAR(100),
    tax_rate FLOAT,
    sqft_basement INT,
    htw VARCHAR(10),
    pool VARCHAR(10),
    commercial VARCHAR(10),
    water VARCHAR(50),
    sewage VARCHAR(50),
    year_built INT,
    sqft_mu INT,
    sqft_total INT,
    parking VARCHAR(50),
    bed INT,
    bath INT,
    basement_yes_no VARCHAR(10),
    layout VARCHAR(50),
    net_yield FLOAT,
    irr FLOAT,
    rent_restricted VARCHAR(10),
    neighborhood_rating INT,
    latitude DOUBLE,
    longitude DOUBLE,
    subdivision VARCHAR(100),
    taxes INT,
    selling_reason TEXT,
    seller_retained_broker TEXT,
    final_reviewer VARCHAR(100),
    school_average FLOAT
);
 
-- 2. Valuation Table
CREATE TABLE valuations (
    valuation_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    list_price FLOAT,
    previous_rent FLOAT,
    arv FLOAT,
    zestimate FLOAT,
    expected_rent FLOAT,
    rent_zestimate FLOAT,
    low_fmr FLOAT,
    high_fmr FLOAT,
    redfin_value FLOAT,
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);
 
-- 3. HOA Table
CREATE TABLE hoa (
    hoa_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    hoa FLOAT,
    hoa_flag VARCHAR(10),
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);
 
-- 4. Rehab Table
CREATE TABLE rehab (
    rehab_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    underwriting_rehab FLOAT,
    rehab_calculation FLOAT,
    paint VARCHAR(10),
    flooring_flag VARCHAR(10),
    foundation_flag VARCHAR(10),
    roof_flag VARCHAR(10),
    hvac_flag VARCHAR(10),
    kitchen_flag VARCHAR(10),
    bathroom_flag VARCHAR(10),
    appliances_flag VARCHAR(10),
    windows_flag VARCHAR(10),
    landscaping_flag VARCHAR(10),
    trashout_flag VARCHAR(10),
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);
