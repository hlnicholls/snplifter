import pytest
from unittest.mock import patch, MagicMock
from snplifter.modules.liftover.liftover import LiftOver

@pytest.fixture
def mock_liftover_init():
    """Fixture to mock the LiftOver initialization process."""
    with patch('snplifter.modules.liftover.liftover.LiftOver._add_liftover_chain') as mock_method:
        yield mock_method

def test_liftover_initialization(mock_liftover_init):
    """
    Test that the LiftOver class initializes correctly, with the Hail interaction mocked.
    """
    chain_file = 'dummy_chain_file'
    input_dir = 'dummy_input_dir'
    output_dir = 'dummy_output_dir'
    liftover_direction = '38to37'
    phenotypes = ['phenotype1', 'phenotype2']

    lo = LiftOver(chain_file, input_dir, output_dir, liftover_direction, phenotypes)

    assert lo.chain_file == chain_file
    assert lo.input_dir == input_dir
    assert lo.output_dir == output_dir
    assert lo.liftover_direction == liftover_direction
    assert lo.phenotypes == phenotypes
    mock_liftover_init.assert_called_once()

def test_liftover_initialization_default_phenotypes(mock_liftover_init):
    """
    Test that the LiftOver class initializes with default phenotypes correctly, with Hail interactions mocked.
    """
    chain_file = 'dummy_chain_file'
    input_dir = 'dummy_input_dir'
    output_dir = 'dummy_output_dir'
    liftover_direction = '38to37'

    lo = LiftOver(chain_file, input_dir, output_dir, liftover_direction)

    assert lo.phenotypes == []
    mock_liftover_init.assert_called_once()
