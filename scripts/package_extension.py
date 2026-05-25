#!/usr/bin/env python3
import os
import zipfile

def package_extension():
    # Define files and directories that belong to the Chrome Extension
    extension_includes = [
        "manifest.json",
        "background.js",
        "cloudflare-temp-email-utils.js",
        "cloudmail-utils.js",
        "gopay-utils.js",
        "hotmail-utils.js",
        "icloud-utils.js",
        "luckmail-utils.js",
        "mail-provider-utils.js",
        "mail2925-utils.js",
        "managed-alias-utils.js",
        "paypal-utils.js",
        "yyds-mail-utils.js",
        "rules.json",
        "background",
        "content",
        "core",
        "flows",
        "icons",
        "imports",
        "phone-sms",
        "shared",
        "sidepanel"
    ]

    output_zip = "flowpilot-extension.zip"
    print(f"Starting to package FlowPilot Chrome Extension into '{output_zip}'...", flush=True)

    if os.path.exists(output_zip):
        os.remove(output_zip)

    count_files = 0
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for item in extension_includes:
            if not os.path.exists(item):
                print(f"Warning: '{item}' not found, skipping.", flush=True)
                continue

            if os.path.isfile(item):
                zip_file.write(item)
                count_files += 1
                print(f"  Added file: {item}", flush=True)
            elif os.path.isdir(item):
                for root, dirs, files in os.walk(item):
                    for file in files:
                        full_path = os.path.join(root, file)
                        # Avoid packaging OS specific files like .DS_Store
                        if file == ".DS_Store":
                            continue
                        zip_file.write(full_path)
                        count_files += 1
                print(f"  Added directory: {item}", flush=True)

    print(f"\nSuccessfully packaged {count_files} files into '{output_zip}'!", flush=True)

if __name__ == "__main__":
    package_extension()
