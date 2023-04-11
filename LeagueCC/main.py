from api_requests import get_summonerID

def main():
    sum_id = get_summonerID(input("Name: "))

if __name__ == "__main__":
    main()
else:
    print(__name__)    