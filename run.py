import providers.google as gfd
import providers.duckduck as ddg

def main():
    # Call functions from the google_finch_download module
    # gfd.main()
    search_term = 'male common yellowthroat'
    file_prefix = 'cy-male'
    target_directory = './downloads'
    max_results = 100
    ddg.download_images(search_term, file_prefix, target_directory, max_results)

if __name__ == "__main__":
    main()