import sys
from opengateway_sandbox_sdk import Simswap

APP_CLIENT_ID = "your-registered-app-client-id"
APP_CLIENT_SECRET = "your-registered-app-client-secret"

def main() -> None:
    phone_number = sys.argv[1]
    max_age = int(sys.argv[2]) if len(sys.argv) > 2 else 2400

    simswap_client = Simswap(APP_CLIENT_ID, APP_CLIENT_SECRET, phone_number)
    print(f'CIBA auth success')

    if simswap_client.check(max_age=2400):
        print(f'A SIM card swap happened in the last {max_age // 24} days')
    else:
        print(f'No SIM card swap in the last {max_age // 24} days')

    last_swap = simswap_client.retrieve_date()
    print(f'Last SIM card swap happened {last_swap}')

if __name__ == "__main__":
    main()
