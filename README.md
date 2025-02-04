# Media_Sorter

**Media_Sorter** is a Python tool designed to help you organize and sort your media files (photos and videos) by their creation or taken date. It scans your media files, extracts metadata (such as EXIF data for photos), and organizes them into folders based on user-defined date and time ranges.

## Features:
- Automatically organizes photos and videos by their creation or taken date.
- Sorts files into subfolders based on user-defined date and time ranges.
- Supports various media formats, including `.jpg`, `.jpeg`, `.png`, `.mp4`, `.mov`, `.avi`, `.mkv`, `.3gp`, `.webm`.
- Reads EXIF metadata for photos and uses file creation date when metadata is unavailable.

## Requirements:
- Python 3.x
- Pillow (Python Imaging Library) to read image EXIF data. Install it using:
  ```bash
  pip install pillow

## How to Save file and folders
        Desktop
    ├── Photos To Sort

## How will it look once everything is sorted
    Desktop
    ├── Photos To Sort
    │   ├── Sorted
    │   │   ├── January_Sort
    │   │   ├── February_Sort
    │   │   └── ...
    │   ├── photo1.jpg
    │   ├── video1.mp4
    │   └── ...

## Supported File Types:
    Photos: .jpg, .jpeg, .png, .gif
    Videos: .mp4, .mov, .avi, .mkv, .3gp, .webm

## Summary
 Key Features:
    Sort media files by date: Automatically organize photos and videos based on when they were taken or created.
    User-defined time ranges: Users can specify a start and end date/time for file sorting.
    Support for multiple file types: Handles various media formats, including images and videos.
    Cross-platform compatibility: Works on both Windows and Linux systems.
    Simple and intuitive: Easily move files into organized subfolders with minimal setup.