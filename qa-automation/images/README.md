# Reference Images for Image Recognition Tests

This directory contains reference images of UI elements used for image recognition-based testing.

## How to Capture Reference Images

To use the image recognition tests, you need to capture reference images of the UI elements first. Follow these steps:

### 1. Build and Run the Application

```bash
# From the universe root directory
npm install
npm run tauri build

# Run the built application
# Windows: src-tauri/target/release/Tari Universe (Alpha).exe
# Linux: src-tauri/target/release/tari-universe-alpha
# macOS: src-tauri/target/release/bundle/macos/Tari Universe (Alpha).app
```

### 2. Capture Screenshots

Run the application and use a screenshot tool to capture individual UI elements:

#### Required Images:

1. **mining_button.png** - The main mining start/stop button
   - Capture the entire button including text and icon
   - Should be captured when button is in idle state

2. **cpu_tile.png** - The CPU mining tile in the sidebar
   - Capture the entire tile including icon and text
   - Should show "CPU" label clearly

3. **gpu_tile.png** - The GPU mining tile in the sidebar
   - Capture the entire tile including icon and text
   - Should show "GPU" label clearly

4. **settings_icon.png** - The settings icon/button
   - Capture just the icon or button
   - Usually found in top-right or sidebar

5. **logo.png** - The Tari Universe logo
   - Capture the logo from the application window
   - Usually in the top-left or sidebar

### 3. Image Capture Tips

- **Size**: Capture the smallest region that uniquely identifies the element
- **Quality**: Use PNG format for best quality
- **State**: Capture elements in their default/idle state
- **Consistency**: Ensure good contrast and no overlapping elements
- **Resolution**: Capture at the same resolution you'll run tests at

### 4. Using Screenshot Tools

#### Windows
- Use Snipping Tool or Snip & Sketch
- Press `Win + Shift + S` to capture a region
- Save as PNG in this directory

#### macOS
- Press `Cmd + Shift + 4` to capture a region
- Files are saved to Desktop by default
- Move to this directory and rename appropriately

#### Linux
- Use `gnome-screenshot -a` or similar tool
- Or use `scrot -s` for region selection
- Save as PNG in this directory

### 5. Verify Images

After capturing, verify the images work:

```bash
cd qa-automation
python3 -m pytest tests/test_image_recognition.py -v
```

## Image Naming Convention

- Use lowercase with underscores
- Be descriptive: `mining_button.png`, not `button1.png`
- Include state if relevant: `mining_button_active.png`

## Optional Images

You can capture additional images for more comprehensive testing:

- `mining_button_active.png` - Mining button when mining is active
- `mining_button_paused.png` - Mining button when mining is paused
- `eco_mode_icon.png` - Eco mode indicator
- `ludicrous_mode_icon.png` - Ludicrous mode indicator
- `earnings_display.png` - Earnings number display area
- `sync_indicator.png` - Blockchain sync indicator

## Troubleshooting

### Image Not Found
- Check that the image file exists in `qa-automation/images/`
- Verify the filename matches exactly (case-sensitive)

### Image Recognition Fails
- Try adjusting the confidence threshold in `config.yaml`
- Recapture the image with better contrast
- Ensure the UI element is fully visible and not obscured
- Check that the application is in the same state as when you captured the image

### Low Confidence Matches
- Increase image size to include more context
- Ensure the element is captured at the same zoom/scale
- Try grayscale matching by setting `grayscale: true` in config.yaml
