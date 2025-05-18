"""Provides a filter for NPK entries in the NPK file list."""

from core.npk.enums import NPKEntryFileType
from gui.utils.npk import get_npk_file, ransack_agent
from gui.widgets.npk_file_list import NPKFileList

class NPKEntryFilter:
    """
    This class is used to filter NPK entries based on given conditions.
    """

    def __init__(self, list_view: NPKFileList):
        self._list_view = list_view
        self.filter_string = ""
        self.filter_type: NPKEntryFileType | None = None

        self.mesh_biped_head = False

    def apply_filter(self):
        """
        Filters the NPK entries based on the filter string.

        :param npk_entries: List of NPK entries to be filtered.
        :return: Filtered list of NPK entries.
        """
        model = self._list_view.model()
        npk_file = get_npk_file()
        if not model or not npk_file:
            return

        for row in range(model.rowCount()):
            npk_entry = npk_file.read_entry(row)
            filename_lower = model.get_filename(model.index(row)).lower()

            # Text filter - quick reject
            if self.filter_string and self.filter_string not in filename_lower:
                self._list_view.setRowHidden(row, True)
                continue

            # Category filtering
            if self.filter_type is None:
                # No filter type set, show all
                show_item = True
            elif self.filter_type == npk_entry.file_type:
                if self.filter_type == NPKEntryFileType.MESH:
                    # Only do the expensive biped head check if needed
                    show_item = not self.mesh_biped_head or ransack_agent(npk_entry.data, "biped head")
                else:
                    show_item = True
            else:
                show_item = False

            # Apply visibility
            self._list_view.setRowHidden(row, not show_item)
