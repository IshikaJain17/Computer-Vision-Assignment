                                                     Pencil Length and Angle Estimation using Computer Vision
Overview
This project focuses on using computer vision techniques to analyze an image containing two pencils (labeled as Pencil A and Pencil B) positioned at an angle. The objectives include determining the lengths of both pencils, calculating the angle between them, and highlighting the region where the pencils intersect.

Problem Statement
Given an image:

Identify and measure the lengths of Pencil A and Pencil B (assuming 1 pixel = 0.1 mm).
Calculate the angle at which Pencil A and Pencil B are placed relative to each other.
Highlight the region where the pencils intersect.
Approach
Image Processing: Use Python libraries like OpenCV for reading the image and performing operations such as edge detection, contour detection, and region highlighting.

Length Estimation: Measure the lengths of Pencil A and Pencil B by identifying their longest dimensions in pixels and converting to millimeters using the given scale (1 pixel = 0.1 mm).

Angle Calculation: Determine the angle between Pencil A and Pencil B using geometric methods such as vector calculations or line fitting.

Intersection Highlighting: Highlight the region where the pencils overlap or intersect using techniques like masking or drawing contours.

Implementation Details
Programming Language: Python
Libraries Used: OpenCV, NumPy
Assumptions: 1 pixel = 0.1 mm for length estimation.
Outputs: Lengths of Pencil A and Pencil B, angle between the pencils, and a visual representation of their intersection.
Usage
Installation: Ensure Python and required libraries (OpenCV, NumPy) are installed.

Execution: Run the script or notebook provided (pencil_analysis.py or pencil_analysis.ipynb).

Input: Provide an image containing the pencils positioned at an angle.

Output: The script will output the lengths of Pencil A and Pencil B, the calculated angle between them, and a visual representation of their intersection.

Example

In this example, after running the script, the output might be:

Length of Pencil A: 55 mm
Length of Pencil B: 45 mm
Angle between Pencil A and Pencil B: 30 degrees
Highlighted region of intersection: Highlighted in the output image.
Contributor
ISHIKA JAIN
License
This project is licensed under the MIT License - see the LICENSE file for details.

