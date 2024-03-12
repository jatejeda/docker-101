import requests
import pandas as pd

url = 'https://charts-spotify-com-service.spotify.com/public/v0/charts'


def main():
    response = requests.get(url)
    chart = []
    for entry in response.json()['chartEntryViewResponses'][0]['entries']:
        chart.append({
            "Rank": entry['chartEntryData']['currentRank'],
            "Artist": ', '.join([artist['name'] for artist in entry['trackMetadata']['artists']]),
            "TrackName": entry['trackMetadata']['trackName']
        })
    df = pd.DataFrame(chart)
    print(df.to_string(index=False))


if __name__ == '__main__':
    main()
