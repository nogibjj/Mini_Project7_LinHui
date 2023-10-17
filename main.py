import sqlite3

conn = sqlite3.connect('Deaths&Insurance.db')
cursor = conn.cursor()

streamlined_query_2015 = """
    SELECT 
        ped.State,
        SUM(ped.ObservedDeaths) AS Total_ObservedDeaths,
        SUM(ped.PotentiallyExcessDeaths) AS Total_PotentiallyExcessDeaths,
        AVG(ped.PercentPotentiallyExcessDeaths) AS Avg_PercentPotentiallyExcessDeaths,
        hic."UninsuredRate(2015)" AS UninsuredRate_2015,
        hic."HealthInsuranceCoverageChange(2010-2015)" AS HealthInsuranceCoverageChange_2010_2015,
        hic."EmployerHealthInsuranceCoverage(2015)" AS EmployerCoverage_2015
    FROM 
        Potentially_excess_deaths ped
    JOIN 
        Health_Insurance_Coverage hic ON ped.State = hic.State
    WHERE
        ped.Year = 2015
    GROUP BY 
        ped.State
    ORDER BY 
        Total_PotentiallyExcessDeaths DESC;
"""

streamlined_query_2015_results = cursor.execute(streamlined_query_2015).fetchall()
print(streamlined_query_2015_results[:5])

cursor.close()
conn.close()