
class OldTurkicConverter:
    """Converter for Azerbaijani Latin script -> Old Turkic runes."""

    _map = {
        'a': '𐰀',
        'ə': '𐰂',
        'b': '𐰉',
        'c': '𐰕',
        'ç': '𐰲',
        'd': '𐰑',
        'e': '𐰅',
        'f': '𐰊',
        'g': '𐰏',
        'ğ': '𐰍',
        'h': '𐰎',
        'ı': '𐰃',
        'i': '𐰄',
        'k': '𐰚',
        'l': '𐰞',
        'm': '𐰢',
        'n': '𐰣',
        'o': '𐰗',
        'ö': '𐰘',
        'p': '𐰯',
        'q': '𐰴',
        'r': '𐰺',
        's': '𐰽',
        'ş': '𐱁',
        't': '𐱃',
        'u': '𐰆',
        'ü': '𐰈',
        'v': '𐰋',
        'x': '𐰐',
        'y': '𐰖',
        'z': '𐰔'
    }

    @classmethod
    def convert(cls, text: str) -> str:
        """Convert Azerbaijani Latin text into Old Turkic runes."""
        result = ""
        for char in text.lower():
            result += cls._map.get(char, char)  # fallback: keep char as is
        return result
