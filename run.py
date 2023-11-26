import providers.google as gfd
import providers.duckduck as ddg

def get_ddgfinches():
    finches = [
        ("female house finch", "house_finch-female"),
        ("female purple finch", "purple_finch-female"),
        ("female cassin's finch", "cassins_finch-female"),
        ("female pine siskin", "pine_siskin-female"),
    ]
    for search_term, file_prefix in finches:
        target_directory = './downloads'
        max_results = 200
        ddg.download_images(search_term, file_prefix, target_directory, max_results)

def main():
    # google functions
    # gfd.main()
    # duckduckgo functions
    get_ddgfinches()

if __name__ == "__main__":
    main()