# Pentatonic Shapes Quiz

A GUI-based flashcard quiz application for learning and practicing the 5 pentatonic box shapes for guitar. Created with Claude Sonnet 4.

## Features

- **Interactive GUI**: Clean, modern interface with dark theme
- **Random Quiz Generation**: 50 random questions per session from 5 pentatonic shapes
- **Image Display**: Shows pentatonic shape diagrams with random 180° rotation for added challenge
- **Keyboard Navigation**: Complete the entire quiz using only keyboard (Enter key)
- **Immediate Feedback**: Shows correct answer immediately if you're wrong
- **Performance Tracking**: Detailed results showing accuracy per shape
- **No Data Storage**: Results are session-only with no long-term storage

## Requirements

- Python 3.6+
- tkinter (usually included with Python)
- Pillow (PIL) for image handling

## Installation

1. Clone or download this repository
2. Install required packages:
   ```bash
   pip install pillow
   ```
3. Ensure you have your pentatonic shape images named `shape1.jpg` through `shape5.jpg` in the same directory

## Usage

Run the program:
```bash
python pentatonic_quiz.py
```

### How to Use

1. **Start Quiz**: The program automatically starts with the first question
2. **Answer Questions**: 
   - Look at the displayed pentatonic shape image
   - Enter a number (1-5) corresponding to which shape you think it is
   - Press **Enter** to submit your answer
3. **View Feedback**: See if you're correct or view the right answer
4. **Continue**: Press **Enter** again to move to the next question
5. **Complete Session**: After 50 questions, view your detailed results
6. **Restart**: Option to start a new quiz session

### Keyboard Shortcuts

- **Enter**: Submit answer / Move to next question
- **Numbers 1-5**: Enter your shape guess
- **Mouse**: Optional - you can also click the Submit and Next buttons

## File Structure

```
pentashapes/
├── pentatonic_quiz.py      # Main application
├── README.md               # This file
├── shape1.jpg              # Pentatonic shape 1 image
├── shape2.jpg              # Pentatonic shape 2 image
├── shape3.jpg              # Pentatonic shape 3 image
├── shape4.jpg              # Pentatonic shape 4 image
└── shape5.jpg              # Pentatonic shape 5 image
```

## Features in Detail

### Random Rotation
- Images are randomly rotated 180° (upside-down) with 50% probability
- This increases difficulty and helps develop pattern recognition from different orientations

### Progress Tracking
- Shows current question number (e.g., "Question 15 of 50")
- Real-time feedback on each answer

### Results Summary
- Overall accuracy percentage
- Per-shape performance breakdown
- Shows how many times each shape appeared and your accuracy for each

### User-Friendly Design
- Large, clear images with proper scaling
- High contrast colors for readability
- Responsive layout that works on different screen sizes

## Customization

You can easily modify the program:

- **Change quiz length**: Modify `self.total_questions = 50` in the code
- **Add more shapes**: Add more image files and update the range in the file checking loop
- **Adjust image size**: Change `max_width, max_height = 400, 300` values
- **Modify colors**: Update the color codes in the GUI setup

## Troubleshooting

### Common Issues

1. **"Image file not found" error**:
   - Ensure all files `shape1.jpg` through `shape5.jpg` exist in the same directory as the Python script
   - Check file names are exactly correct (case-sensitive on some systems)

2. **Images not displaying properly**:
   - Make sure Pillow is installed: `pip install pillow`
   - Verify image files are valid JPEG format

3. **GUI appears too small/large**:
   - Adjust the window size in the code: `self.root.geometry("800x700")`

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Additional image formats support
- More customization options
- Different quiz modes
- Score saving features
- Additional rotation angles

## Author

Created for guitar players learning pentatonic scale patterns and shapes.
