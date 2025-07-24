#!/bin/sh

# Function to display usage
show_usage() {
    echo "Usage: $0 [OPTIONS] <URL>"
    echo ""
    echo "Options:"
    echo "  -u, --user-agent <agent>    Custom user agent (default: Chrome 120.0.0.0)"
    echo "  -h, --help                  Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 https://topcv.vn"
    echo "  $0 -u 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' https://topcv.vn"
    echo ""
}

# Default values
USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
TARGET_URL=""

# Parse command line arguments
while [ $# -gt 0 ]; do
    case $1 in
        -u|--user-agent)
            USER_AGENT="$2"
            shift 2
            ;;
        -h|--help)
            show_usage
            exit 0
            ;;
        -*)
            echo "Unknown option: $1"
            show_usage
            exit 1
            ;;
        *)
            if [ -z "$TARGET_URL" ]; then
                TARGET_URL="$1"
            else
                echo "Error: Multiple URLs provided. Only one URL is allowed."
                exit 1
            fi
            shift
            ;;
    esac
done

# Check if URL is provided
if [ -z "$TARGET_URL" ]; then
    echo "Error: URL is required"
    show_usage
    exit 1
fi

# Execute chromium with the provided parameters
/snap/bin/chromium --headless=new --no-sandbox --disable-gpu --user-agent="$USER_AGENT" --disable-extensions --disable-plugins --disable-images --disable-javascript --dump-dom "$TARGET_URL"