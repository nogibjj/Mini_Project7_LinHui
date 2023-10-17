
import sqlite3

def connect_to_db(db_path):
    return sqlite3.connect(db_path)
def fetch_data_for_year_2015(cursor):
    streamlined_query_2015 = '''
        SELECT
            ped.State,
            SUM(ped.ObservedDeaths) AS Total_ObservedDeaths,
            SUM(ped.PotentiallyExcessDeaths) AS Total_PotentiallyExcessDeaths,
            AVG(ped.PercentPotentiallyExcessDeaths) AS
                    Avg_PercentPotentiallyExcessDeaths,
            hic."UninsuredRate(2015)" AS UninsuredRate_2015,
            hic."HealthInsuranceCoverageChange(2010-2015)" AS
                    HealthInsuranceCoverageChange_2010_2015,
            hic."EmployerHealthInsuranceCoverage(2015)" AS
                    EmployerCoverage_2015
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
    '''
    return cursor.execute(streamlined_query_2015).fetchall()

def main():
    db_path = 'Deaths&Insurance.db'
    conn = connect_to_db(db_path)
    cursor = conn.cursor()

    results = fetch_data_for_year_2015(cursor)
    print(results[:5])

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
