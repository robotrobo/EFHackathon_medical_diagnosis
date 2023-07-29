from faster_whisper import WhisperModel
import logging


TRANSCRIPT_MODEL_SIZE = "tiny.en"
MAX_RETRIES_TRANSCRIPTION = 3
TIMEOUT_TRANSCRIPTION =  5

logging.basicConfig()
logging.getLogger("faster_whisper").setLevel(logging.DEBUG)

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("Function call timed out")



def initialize_model():
    model = WhisperModel(TRANSCRIPT_MODEL_SIZE,
                                 device="cpu", compute_type="int8")
    return model

def create_transcription(audio_file) -> str:
    model = initialize_model()

    if model is None:
        print("Failed to initialize transcription model. Probably a problem with the socket.")
        exit(1)

    segments, info = model.transcribe(audio_file, beam_size=5)

    print("Detected language '%s' with probability %f" %
          (info.language, info.language_probability))

    print("Beginning transcription...")

    segments = list(segments)

    return "".join([f"\n({seg.start:.2f}:{seg.end:.2f})" + seg.text for seg in segments])

