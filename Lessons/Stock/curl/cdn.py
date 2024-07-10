import requests

def get_cdn_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Content successfully retrieved from CDN.")
        print("\nCDN Information:")
        
        # Common CDN-related headers
        cdn_headers = [
            'CF-Cache-Status',   # Cloudflare
            'X-Cache',           # Various CDNs like AWS CloudFront
            'X-CDN',             # Various CDNs
            'X-Cache-Status',    # Various CDNs
            'Via',               # General header showing proxy/CDN details
            'Server',            # Server header often reveals CDN
            'X-Akamai-Transformed',  # Akamai
            'X-Fastly-Request-ID'    # Fastly
        ]
        
        for header in cdn_headers:
            if header in response.headers:
                print(f"{header}: {response.headers[header]}")
                
        print("\nFull Headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")

if __name__ == "__main__":
    url = "https://www.facebook.com"  # Replace with a URL served through a CDN
    get_cdn_info(url)
