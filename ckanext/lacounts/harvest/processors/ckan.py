import logging
from urlparse import urljoin
from ckanext.lacounts.harvest import helpers
log = logging.getLogger(__name__)


def ckan_processor(package, harvest_object):

    # Pre-map
    package['harvest_dataset_url'] = '{harvest_source_url}/dataset/{id}'.format(**package)

    # Map
    package = helpers.map_package(package, {
        # Contact
        'contact_name': ['contact_name'],
        'contact_email': ['contact_email'],
        # Temporal
        'temporal_text': ['temporal_coverage'],
        'temporal_start': [],
        'temporal_end': [],
        # Spatial
        'spatial_text': ['geo_coverage', 'spatial_coverage'],
        'spatial': [],
        # Frequency
        'frequency': ['accrual_periodicity', 'frequency'],
        # Provenance
        'provenance': ['author', 'program'],
    })

    # Post-map
    package['frequency'] = helpers.normalize_frequency(package.get('frequency'))

    return package
