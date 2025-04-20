import pandas as pd


def load_and_merge_data():
    # Load individual CSVs
    driver_standings = pd.read_csv('./data/driver_standings.csv')
    drivers = pd.read_csv('./data/drivers.csv')
    races = pd.read_csv('./data/races.csv')

    # Keep only necessary columns
    drivers_subset = drivers[['driverId', 'driverRef']]
    races_subset = races[['raceId', 'year']]

    # Merge drivers
    merged_data = driver_standings.merge(
        drivers_subset, on='driverId', how='left'
    )

    # Merge races
    merged_data = merged_data.merge(
        races_subset, on='raceId', how='left'
    )

    return merged_data


if __name__ == "__main__":
    combined_data = load_and_merge_data()
    combined_data.to_csv('./data/combined_driver_standings.csv', index=False)
