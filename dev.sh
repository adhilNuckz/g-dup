#!/bin/bash
# DUP Development Helper Script for Linux

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions
print_header() {
    echo "================================================"
    echo "DUP - Drive Upload Program"
    echo "Development Helper Script"
    echo "================================================"
    echo ""
}

print_success() {
    echo -e "${GREEN}SUCCESS:${NC} $1"
}

print_error() {
    echo -e "${RED}ERROR:${NC} $1"
}

print_info() {
    echo -e "${BLUE}INFO:${NC} $1"
}

install_dev() {
    print_info "Installing DUP in development mode..."
    pip install -e .
    print_success "DUP installed in development mode"
    echo ""
    echo "Run 'dup login' to get started"
}

build_binary() {
    print_info "Building Linux binary..."
    pip install pyinstaller
    pyinstaller --onefile dup/__main__.py --name dup
    print_success "Binary created at dist/dup"
    echo ""
    echo "To install: sudo cp dist/dup /usr/local/bin/"
}

run_tests() {
    print_info "Running DUP commands..."
    echo ""
    
    echo "Testing version..."
    dup version
    echo ""
    
    echo "Testing pwd..."
    dup pwd
    echo ""
    
    echo "Testing ls..."
    dup ls
    echo ""
    
    print_success "All basic tests completed"
}

clean_build() {
    print_info "Cleaning build artifacts..."
    rm -rf build/
    rm -rf dist/
    rm -f dup.spec
    find . -type f -name "*.pyc" -delete
    find . -type d -name "__pycache__" -delete
    find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
    print_success "Cleaned build directories"
}

run_dup() {
    print_info "Running DUP..."
    python -m dup "$@"
}

show_help() {
    echo "Usage: ./dev.sh [command] [options]"
    echo ""
    echo "Commands:"
    echo "  install   - Install DUP in development mode"
    echo "  build     - Build Linux binary"
    echo "  test      - Run basic tests"
    echo "  clean     - Clean build artifacts"
    echo "  run       - Run DUP (e.g., ./dev.sh run login)"
    echo "  help      - Show this help message"
    echo ""
    echo "Examples:"
    echo "  ./dev.sh install"
    echo "  ./dev.sh build"
    echo "  ./dev.sh run login"
    echo "  ./dev.sh run ls"
    echo "  ./dev.sh clean"
}

# Main script
print_header

case "$1" in
    install)
        install_dev
        ;;
    build)
        build_binary
        ;;
    test)
        run_tests
        ;;
    clean)
        clean_build
        ;;
    run)
        shift
        run_dup "$@"
        ;;
    help|--help|-h|"")
        show_help
        ;;
    *)
        print_error "Unknown command: $1"
        echo ""
        show_help
        exit 1
        ;;
esac

echo ""
echo "================================================"
