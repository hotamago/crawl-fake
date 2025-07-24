#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import time
import subprocess
import os
import shlex
from typing import Optional
from fake_useragent import UserAgent

def crawl_topcv_direct_command(url: str, timeout: int = 30) -> Optional[str]:
    """
    Direct command execution with command line parameters
    """
    # Generate random user agent
    agent_ran = UserAgent(browsers=['Edge', 'Chrome'], platforms='desktop', min_version=134.0).random
    print(f"Using Agent: {agent_ran}")
    
    # Build command with parameters
    cmd = [
        "sh",
        "cli.sh",
        "--user-agent", agent_ran,
        url
    ]
    
    try:
        # Start timing the subprocess
        start_time = time.time()
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        # if result.stderr:
        #     print(f"Stderr content: {result.stderr}")
        
        if result.returncode == 0:
            return result.stdout
        else:
            return None
            
    except subprocess.TimeoutExpired as e:
        print(f"Command timed out after {timeout} seconds")
        print(f"Timeout exception details: {e}")
        return None
    except FileNotFoundError as e:
        print(f"Command not found: {e}")
        print("Make sure 'sh' is available in your system PATH")
        return None
    except PermissionError as e:
        print(f"Permission denied: {e}")
        print("Make sure cli.sh has execute permissions")
        return None
    except Exception as e:
        print(f"Unexpected error occurred while running command: {e}")
        print(f"Error type: {type(e).__name__}")
        return None


if __name__ == "__main__":
    url = "https://www.topcv.vn/viec-lam/nhan-vien-ke-toan-cong-truong-tu-02-nam-kinh-nghiem-thu-nhap-den-15-trieu-tai-my-loc-nam-dinh/1811427.html?ta_source=BoxFeatureJob_LinkDetail"
    
    time_start = time.perf_counter()
    
    # Try the direct command approach first
    print("=== Trying direct command approach ===")
    html_content = crawl_topcv_direct_command(url, timeout=30)
    
    if html_content:
        print("Successfully retrieved HTML content")
        print(f"HTML length: {len(html_content)} characters")
        print(f"HTML preview: {html_content[-500:]}")
    else:
        print("Failed to retrieve HTML content with direct command")
    
    time_end = time.perf_counter()
    print(f"\nTotal time taken: {time_end - time_start:.4f} seconds") 