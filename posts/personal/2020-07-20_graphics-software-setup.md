---
tags:
  - art resources
  - resource
---

# Graphics Software Setup

This is a collection of settings I use in various graphics software programs. Note that my setup is tailored to my specific learning path, so they may not be best suited for your exact circumstances. However, I think these resources are still worth sharing.

Last edited: 2024-06-10

## Photoshop

### Setup

- Edit > Preferences > General > Color Picker > Windows (Preference from MS Paint)
- Edit > Preferences > General > Image Interpolation > Nearest Neighbor (makes transformations pixel-perfect instead of smooth, essential for pixel art)
- Edit > Preferences > General > Zoom with Scroll Wheel > checked
- Edit > Preferences > Displays & cursors > Other cursors > Precise (makes it easier to pick the right color using the eyedropper)
- Edit > Preferences > Units and Rulers > Rulers > Pixels
- ~~Edit > Keyboard shortcuts... > Edit > Step Forward > Ctrl + Y~~
- Edit > Keyboard shortcuts... > Edit > Step Backward > Ctrl + Z
- Edit > Color settings... RGB > Monitor RGB (prevents colors from changing when exporting PSD as PNG)

### Tools

- Brush > caret > small thumbnail
- Eraser > Block mode: scale eraser depending on zoom
- History > checkbox (turns into an icon with a paintbrush and arrow): pin edit as the "last good version" of your image, even after you exceed your edit history limit
- Move > right click: jump to any layer with the pixel you clicked on filled
- Window > Arrange > New Window: create a resizable thumbnail for that file, so you don't have to zoom in/out all of the time
- Thumbnail > Zoom > 50%, 25%, 12.5%, etc.: render what your final image will look like when exported, since the thumbnail is "smoother" than any other zoom due to the different interpolation algorithm being used

### Generally useful shortcuts

- Shift + [tool]: toggles between all tools associated with that shortcut key (e.g., G to select gradient tool, then Shift + G to toggle it to Paint Bucket)
- Alt + click: turns Cancel buttons into Reset buttons
- D: reset current foreground/background color to default (black/white)
- X: flip current foreground/background color
- Ctrl + T: free transform your current selection
- Canvas > Ctrl + Drag: move current layer (faster than switching to Move tool)
- Canvas > Space + Drag: pan around image (faster than switching to Hand tool)
- Canvas > Ctrl + +: zoom in to nearest "sharpest" zoom %
- Canvas + Ctrl + -: zoom out to nearest "sharpest" zoom %
- Canvas > Ctrl + 0: zoom to actual size

### Tool-specific shortcuts

- Brush > Alt + Click: use eyedropper (faster than switching to Eyedropper tool)
- Brush > Alt > Right Click: change brush size (faster than [ + ] shortcuts)
- Brush > Shift + Click: draw straight lines
- Brush > Shift + Drag: draw orthogonal lines
- Layer > Ctrl + Click: select all pixels in that layer
- Layer > Alt + Click: toggle visibility of all other layers
- Layer > Mask > Alt + Click: see the layer directly
- Selection > Ctrl + Arrow Key: nudge selection
- Selection > Ctrl + Shift + Arrow Key: nudge selection a lot
- Selection > Ctrl + Shift + I: invert selection
- Selection Tool > Add to selection (set as default)
- Selection tool > Alt + Drag to subtract from the selection (faster than switching to Subtract mode)

Credits not linked above:

- [PE: 10 tips and tricks not very known about PS](https://www.deviantart.com/thiefoworld/journal/PE-10-tips-and-tricks-not-very-known-about-PS-341799604).

Edit 2021-02-27: Got a Wacom Intuos 3 6x8 in. tablet.

## Wacom Intuos 3

### Setup

- Tool > Grip pen > Pen > top key: [ (bigger brush)
- Tool > Grip pen > Pen > bottom key: ] (smaller brush)
- Tool > Grip pen > Eraser > Right Click
- Tool > Grip pen > Mapping > Screen Area > Monitor 1
- Tool > Grip pen > Mapping > Force Proportions > checked

Edit 2021-10-25: Upgraded to Photoshop CC.

## Photoshop CC

### Setup

- Color Panel > (hamburger menu) > Color Wheel
- Edit > Preferences > Performance > Cache Levels > 8 (improves zoom interpolation)
- Edit > Preferences > Tools > Flick Panning > unchecked
- Edit > Preferences > Workspace > Open Documents as Tabs > unchecked
- Edit > Keyboard Shortcuts... > Shortcuts For: Tools > Blur Tool > R
- Edit > Keyboard Shortcuts... > Shortcuts For: Tools > Sharpen Tool > R
- Edit > Keyboard Shortcuts... > Shortcuts For: Tools > Smudge Tool > R
- Tool > Move > Auto-Select > unchecked
- View > Show > Pixel Grid > unchecked
- Follow the instructions here to fix eyedropper lag

Edit 2022-06-27: Got a Huion HS610.

## Huion HS610

### Setup

- Digital Pen > Bottom Button > Mouse Right Button

Edit 2023-07-29: Switched to Clip Studio Paint.

## Clip Studio Paint

### Setup

- Color Palette > Switch color wheel to HLS color space
- File > Preferences > Layer/Frame > Name of copies > Do not rename
- File > Shortcut Settings > Options > Drawing Color > Switch main color to black and sub color to white > D
- File > Shortcut Settings > Tools > Airbrush > P
- File > Shortcut Settings > Tools > Blend > R
- File > Shortcut Settings > Tools > Brush > P
- File > Shortcut Settings > Tools > Decoration > P
- File > Shortcut Settings > Tools > Move > Rotate > Delete shortcut
- File > Shortcut Settings > Tools > Pen > B
- File > Shortcut Settings > Tools > Pencil > P
- File > Shortcut Settings > Tools > Selection Area > Delete shortcut
- File > Shortcut Settings > Tools > Selection Area > Lasso > L
- File > Shortcut Settings > Tools > Selection Area > Rectangle > M
- File > Shortcut Settings > Tools > Zoom > /
- Selection Launcher > Menu Commands > Edit > Transform > Mesh Transform
- Tool > Auto Select > Tool Property > Anti-aliasing > Off
- Tool > Auto select > Tool property > Selection mode > Add to selection
- Tool > Blend > Color stretch > 30
- Tool > Eyedropper > Pick color from layer
- Tool > Figure > Direct draw > Straight line > Settings > Unit curve > Snap angle > Eye
- Tool > Lasso > Tool property > Selection mode > Add to
- Tool > Lasso [Mesh Transformation] > Tool property > Drag mode > Drag segment
- Tool > Operation > Object (Text) > Settings > Font > Character spacing > Eye
- Tool > Operation > Object (Text) > Settings > Line space/alignment > Line space > Eye
- Tool > Operation > Object (Text) > Settings > Line space/alignment > How to specify > Eye
- Tool > Operation > Object (Text) > Settings > Text > Background Color > Eye
- Tool > Operation > Object (Text) > Settings > Text > Edge > Eye
- Tool > Operation > Object (Text) > Settings > Text > Edge Color > Eye
- Tool > Pen > Wrench > Blending Mode > Eye
- Tool > Pen > Stabilization > 0
- Tool > Rectangle > Tool property > Selection mode > Add to selection
- Tool > Ruler > Perspective Ruler > Tool property > Create at editing layer > checked
- Tool > Text > Text > Settings > Font > Character spacing > Eye
- Tool > Text > Text > Settings > Line space/alignment > Line space > Eye
- Tool > Text > Text > Settings > Line space/alignment > How to specify > Eye
- Tool > Text > Text > Settings > Text > Background Color > Eye
- Tool > Text > Text > Settings > Text > Edge > Eye
- Tool > Text > Text > Settings > Text > Edge Color > Eye

### Brushes

- [The brush also lazy to do a single thickness paint even watercolor main line (主線も水彩も厚塗りも一本でやる怠けものブラシ) ](https://assets.clip-studio.com/en-us/detail?id=1708873)
- Brush settings > Correction > Enable snapping ([source](https://www.reddit.com/pzbsjw/))
