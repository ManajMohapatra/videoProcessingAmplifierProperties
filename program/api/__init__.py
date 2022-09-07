import os
import pkg_resources
import functools
import comtypes.client
import contextlib


@contextlib.contextmanager
def directory_context(dir):
    orig = os.getcwd()
    os.chdir(dir)
    yield
    os.chdir(orig)


def generate_typelibs():
    fn = functools.partial(
        pkg_resources.resource_filename,
        __name__,
    )
    with directory_context(fn('DirectShow')):
        list(
            map(
                comtypes.client.GetModule,
                [
                    'DirectShow.tlb',
                ],
            )
        )

generate_typelibs()
