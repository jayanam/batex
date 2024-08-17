# Batex - Batch Export as FBX

**Version:** 0.7.0  
**Author:** jayanam, Rodrigo Camacho (forked from jayanam)

## Description

Batex is a Blender add-on that allows for batch exporting selected objects as FBX files. The add-on is particularly useful for exporting multiple objects with specific configurations like centered transforms, applied transforms, smoothing options, and more.

## Features

- Export multiple selected objects as FBX.
- Option to center the transform before exporting.
- Apply transforms like scale and rotation (Experimental).
- Support for different smoothing options (Edge, Face, Normals Only).
- Export rig and animations along with the objects.
- Option to export just one material per object.

## Recent Modifications

### Version 0.7.0

- **Added support for exporting empty objects with children:**
  - Empty objects are now included in the export process, preserving the parent-child relationship when re-importing the FBX files.
  - This ensures that the hierarchy is maintained, even if the parent object is an empty object.

- **Improved error handling for objects without materials:**
  - The export process now checks if an object has mesh data before attempting to access its materials, preventing errors when processing empty objects or other non-mesh types.

## Installation

1. Download the Batex add-on from the repository.
2. Open Blender and go to `Edit > Preferences > Add-ons`.
3. Click `Install` and select the downloaded file.
4. Enable the add-on from the list.

## Usage

1. Open the Batex panel in the 3D view (`N` panel > `Batex`).
2. Set the export folder, and choose your desired options like centering transforms, applying transforms, etc.
3. Select the objects you wish to export.
4. Click `Export` to batch export the selected objects as FBX.

## License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.
