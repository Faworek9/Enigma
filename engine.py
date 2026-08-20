from typing import Dict, List


ALPHABET: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ROTOR_SPECS: Dict[str, Dict[str, str]] = {
    "I": {"wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "notch": "Q"},
    "II": {"wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE", "notch": "E"},
    "III": {"wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO", "notch": "V"},
}

REFLECTOR_B: str = "YRUHQSLDPXNGOKMIEBFZCWVJAT"


class Plugboard:
    """Handles character substitution on input and output."""
    
    def __init__(self, swaps: dict = None) -> None:
        """Initialize plugboard with swap dictionary (e.g., {'A': 'X', 'X': 'A'})."""
        self.swaps = swaps if swaps else {}
        self._build_wiring()
    
    def _build_wiring(self) -> None:
        """Build wiring array from swap dictionary."""
        self.wiring = list(ALPHABET)
        for char, swap in self.swaps.items():
            if char in ALPHABET and swap in ALPHABET:
                idx = ALPHABET.index(char)
                self.wiring[idx] = swap
    
    def substitute(self, char: str) -> str:
        """Substitute character through plugboard wiring."""
        if char not in ALPHABET:
            return char
        return self.wiring[ALPHABET.index(char)]


class Rotor:
    """Represents a single Enigma I rotor with notch turnover and ring setting."""

    def __init__(self, wiring: str, notch: str, position: int = 0, ring_setting: int = 0) -> None:
        self.forward_map = [ALPHABET.index(char) for char in wiring]
        self.reverse_map = [0] * 26
        for idx, mapped in enumerate(self.forward_map):
            self.reverse_map[mapped] = idx

        self.notch_index = ALPHABET.index(notch)
        self.position = position % 26
        self.ring_setting = ring_setting % 26

    def at_notch(self) -> bool:
        """Return True when rotor is at turnover position (adjusted by ring setting)."""
        turnover_position = (self.notch_index - self.ring_setting) % 26
        return self.position == turnover_position

    def forward(self, char: str) -> str:
        """Pass character through rotor in forward direction (keyboard -> reflector)."""
        if char not in ALPHABET:
            return char

        input_idx = ALPHABET.index(char)
        shifted_idx = (input_idx + self.position - self.ring_setting) % 26
        mapped_idx = self.forward_map[shifted_idx]
        output_idx = (mapped_idx - self.position + self.ring_setting) % 26
        return ALPHABET[output_idx]
    
    def backward(self, char: str) -> str:
        """Pass character through rotor in reverse direction (reflector -> keyboard)."""
        if char not in ALPHABET:
            return char

        input_idx = ALPHABET.index(char)
        shifted_idx = (input_idx + self.position - self.ring_setting) % 26
        mapped_idx = self.reverse_map[shifted_idx]
        output_idx = (mapped_idx - self.position + self.ring_setting) % 26
        return ALPHABET[output_idx]
    
    def step(self) -> None:
        """Step rotor by one position."""
        self.position = (self.position + 1) % 26


class Reflector:
    """Represents the reflector (Reflector B)."""
    
    def __init__(self, wiring: str) -> None:
        """Initialize reflector with wiring."""
        self.wiring = [ALPHABET.index(char) for char in wiring]
    
    def reflect(self, char: str) -> str:
        """Reflect character through reflector wiring."""
        if char not in ALPHABET:
            return char
        return ALPHABET[self.wiring[ALPHABET.index(char)]]


class EnigmaEngine:
    """Manages the full Enigma encryption process."""
    
    def __init__(
        self,
        rotor_positions: List[int] = None,
        ring_settings: List[int] = None,
        rotor_order: List[str] = None,
        plugboard_preset: str = "Brak",
    ) -> None:
        """Initialize Enigma I using left-to-right rotor config (slot 1,2,3)."""
        rotor_positions = rotor_positions if rotor_positions else [0, 0, 0]
        ring_settings = ring_settings if ring_settings else [0, 0, 0]
        rotor_order = rotor_order if rotor_order else ["I", "II", "III"]

        if len(rotor_positions) != 3 or len(ring_settings) != 3 or len(rotor_order) != 3:
            raise ValueError("Enigma I requires exactly 3 rotor positions, ring settings, and rotor names.")

        if len(set(rotor_order)) != 3:
            raise ValueError("Rotor order must contain three unique rotors (I, II, III).")

        for rotor_name in rotor_order:
            if rotor_name not in ROTOR_SPECS:
                raise ValueError(f"Unsupported rotor: {rotor_name}")

        self.plugboard = Plugboard(self._get_plugboard_swaps(plugboard_preset))
        # Internal order is right->left because the signal enters the right rotor first.
        self.rotors = []
        for rotor_name, position, ring_setting in reversed(list(zip(rotor_order, rotor_positions, ring_settings))):
            self.rotors.append(
                Rotor(
                    ROTOR_SPECS[rotor_name]["wiring"],
                    ROTOR_SPECS[rotor_name]["notch"],
                    position,
                    ring_setting,
                )
            )
        self.reflector = Reflector(REFLECTOR_B)
    
    def _get_plugboard_swaps(self, preset: str) -> dict:
        """Return swap dictionary for selected plugboard preset."""
        presets = {
            'Domyślny': {'A': 'U', 'U': 'A', 'E': 'I', 'I': 'E'},
            'Szyfr Rejewskiego': {'A': 'X', 'X': 'A', 'M': 'K', 'K': 'M', 'E': 'I', 'I': 'E', 'H': 'U', 'U': 'H'},
            'Płachty Zygalskiego': {'B': 'P', 'P': 'B', 'C': 'J', 'J': 'C', 'D': 'V', 'V': 'D', 'O': 'W', 'W': 'O'},
            'Zegar Różyckiego': {'F': 'Z', 'Z': 'F', 'G': 'Q', 'Q': 'G', 'R': 'T', 'T': 'R', 'L': 'N', 'N': 'L'}
        }
        return presets.get(preset, {})
    
    def encrypt(self, text: str) -> str:
        """Encrypt text through full Enigma I signal path."""
        text = text.upper()
        result = ""
        
        for char in text:
            if char not in ALPHABET:
                result += char
                continue

            self._step_rotors()
            
            # Forward path: Plugboard -> right rotor -> middle rotor -> left rotor -> Reflector
            char = self.plugboard.substitute(char)
            for rotor in self.rotors:
                char = rotor.forward(char)
            char = self.reflector.reflect(char)
            
            # Reverse path: left rotor -> middle rotor -> right rotor -> Plugboard
            for rotor in reversed(self.rotors):
                char = rotor.backward(char)
            char = self.plugboard.substitute(char)
            
            result += char
        
        return result
    
    def _step_rotors(self) -> None:
        """Apply historical Enigma stepping with notch turnover and double-stepping."""
        right_rotor = self.rotors[0]
        middle_rotor = self.rotors[1]
        left_rotor = self.rotors[2]

        middle_at_notch = middle_rotor.at_notch()
        right_at_notch = right_rotor.at_notch()

        if middle_at_notch:
            left_rotor.step()
            middle_rotor.step()
        elif right_at_notch:
            middle_rotor.step()

        right_rotor.step()

    def get_rotor_positions(self) -> List[int]:
        """Return current rotor positions in slot order (1, 2, 3)."""
        # Internal order is right->left (slot 3, 2, 1), so reverse to get slot 1, 2, 3
        return [rotor.position for rotor in reversed(self.rotors)]
