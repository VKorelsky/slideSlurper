# Slide Slurper

<img src="https://3.bp.blogspot.com/-HpALEpUJ15E/VPN6m4oD5lI/AAAAAAAAOLE/GFmlj4TWE6w/s1600/slurp-through-a-straw.jpg" width="200">

Pass a video of lecture slides to the slurper and it will give you a pdf of the slides used

## Installation

```
$ pipx install slideSlurper
```

or clone the repository, [install uv](https://docs.astral.sh/uv/getting-started/installation/) and

```
$ uv venv
$ uv sync
$ uv run slurp video_file_path output_pdf_name
```

## Usage

```
$ slurp video_file_path output_pdf_name
```

## Notes

- works best with mp4 video files
