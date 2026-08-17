from typing import List


ALPHABET: List[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class Plugboard:
    """Handles character substitution on input and output."""
    
    def __init__(self, swaps: dict = None) -> None:
        """Initialize plugboard with swap dictionary (e.g., {'A': 'X', 'X': 'A'})."""
        self.swaps = swaps if swaps else {}
        self._build_wiring()
    
    def _build_wiring(self) -> None:
        """Build wiring array from swap dictionary."""
        self.wiring = ALPHABET.copy()
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
    """Represents a single Enigma rotor with wiring and rotation."""
    
    def __init__(self, wiring: List[str], start_offset: int = 0) -> None:
        """Initialize rotor with wiring and starting offset (0-25)."""
        self.wiring = wiring.copy()
        self.start_offset = start_offset
        self.rotation_count = 0
        self._set_start_position()
    
    def _set_start_position(self) -> None:
        """Shift wiring to match starting offset (0 = no rotation, 1-25 = steps)."""
        for _ in range(self.start_offset):
            self.wiring = [self.wiring[-1]] + self.wiring[:-1]
    
    def forward(self, char: str) -> str:
        """Pass character through rotor in forward direction."""
        if char not in ALPHABET:
            return char
        return self.wiring[ALPHABET.index(char)]
    
    def backward(self, char: str) -> str:
        """Pass character through rotor in reverse direction."""
        if char not in ALPHABET:
            return char
        return ALPHABET[self.wiring.index(char)]
    
    def rotate(self) -> None:
        """Rotate rotor by one position using modulo arithmetic."""
        self.wiring = [self.wiring[-1]] + self.wiring[:-1]
        self.rotation_count += 1
    
    def reset_rotation_count(self) -> None:
        """Reset rotation count to zero."""
        self.rotation_count = 0


class Reflector:
    """Represents the reflector (Reflector B)."""
    
    def __init__(self, wiring: List[str]) -> None:
        """Initialize reflector with wiring."""
        self.wiring = wiring
    
    def reflect(self, char: str) -> str:
        """Reflect character through reflector wiring."""
        if char not in ALPHABET:
            return char
        return self.wiring[ALPHABET.index(char)]


class EnigmaEngine:
    """Manages the full Enigma encryption process."""
    
    def __init__(self, rotor1_pos: int = 0, rotor2_pos: int = 0, rotor3_pos: int = 0, plugboard_preset: str = 'Brak') -> None:
        """Initialize Enigma engine with configurable rotor positions (0-25) and plugboard preset."""
        rotor_i_wiring = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
        rotor_ii_wiring = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
        rotor_iii_wiring = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
        reflector_b_wiring = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']
        
        self.plugboard = Plugboard(self._get_plugboard_swaps(plugboard_preset))
        self.rotor1 = Rotor(rotor_i_wiring, rotor1_pos)
        self.rotor2 = Rotor(rotor_ii_wiring, rotor2_pos)
        self.rotor3 = Rotor(rotor_iii_wiring, rotor3_pos)
        self.reflector = Reflector(reflector_b_wiring)
    
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
        """Encrypt text through full Enigma path with rotor cascade."""
        text = text.upper()
        result = ""
        
        for char in text:
            if char not in ALPHABET:
                result += char
                continue
            
            # Forward path: Plugboard -> Rotor1 -> Rotor2 -> Rotor3 -> Reflector
            char = self.plugboard.substitute(char)
            char = self.rotor1.forward(char)
            char = self.rotor2.forward(char)
            char = self.rotor3.forward(char)
            char = self.reflector.reflect(char)
            
            # Reverse path: Rotor3 -> Rotor2 -> Rotor1 -> Plugboard
            char = self.rotor3.backward(char)
            char = self.rotor2.backward(char)
            char = self.rotor1.backward(char)
            char = self.plugboard.substitute(char)
            
            result += char
            
            # Cascade rotor rotation
            self._rotate_rotors()
        
        return result
    
    def _rotate_rotors(self) -> None:
        """Handle cascading rotor rotation."""
        self.rotor1.rotate()
        
        if self.rotor1.rotation_count == 26:
            self.rotor2.rotate()
            self.rotor1.reset_rotation_count()
        
        if self.rotor2.rotation_count == 26:
            self.rotor3.rotate()
            self.rotor2.reset_rotation_count()
